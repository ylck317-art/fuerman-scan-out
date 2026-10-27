#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPC workbench live API: Feishu bitable → JSON for the SPA."""
from __future__ import annotations

import os
import time
from collections import OrderedDict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

APP_ID = os.environ.get("FEISHU_APP_ID", "cli_aa6aa3fddbb81c1e")
APP_SECRET = os.environ.get("FEISHU_APP_SECRET", "")
BITABLE = os.environ.get("FEISHU_BITABLE_APP_TOKEN", "KvnVbzkAWab2sQsaqTQcn3csnwc")
CACHE_TTL = int(os.environ.get("FEISHU_CACHE_TTL", "60"))
TZ_SH = timezone(timedelta(hours=8))

STATIC_DIR = Path(__file__).resolve().parent / "static"

TABLES = {
    "nav": "导航菜单",
    "quick_links": "网页版快捷入口",
    "managers": "部门负责人",
    "settings": "工作台设置",
    "platforms": "平台",
    "stores": "店铺",
    "products": "商品中心",
    "orders": "订单中心",
    "aftersales": "售后工单",
    "campaigns": "推广活动",
    "materials": "知识素材库",
    "ad_daily": "广告投放日报",
    "todos": "待办事项",
    "customers": "客户管理",
    "documents": "单据制作",
    "sales_zhang": "蒙文菲-每日销售",
    "sales_li": "邓帅-每日销售",
    "sales_wang": "姜夏宁-每日销售",
    "adreq_zhang": "蒙文菲-广告费申请表",
    "adreq_li": "邓帅-广告费申请表",
    "adreq_wang": "姜夏宁-广告费申请表",
}

MANAGER_FOR_SALES = {
    "sales_zhang": "张三",
    "sales_li": "李四",
    "sales_wang": "王五",
}

MANAGER_MAP = OrderedDict([
    ("蒙文菲", "张三"),
    ("邓帅", "李四"),
    ("姜夏宁", "王五"),
    ("廖淑萍", "赵六"),
])

SHOP_MAP = OrderedDict([
    ("SMT TOP Accessory", "SMT TOP Acso"),
    ("SMT Arita 3c", "SMTArlic 3c"),
    ("SMTArita 3c", "SMTArlic 3c"),
    ("SMT T-Strap", "SMT T-Stp"),
    ("SMT X-Wrist", "SMT X-Wroit"),
    ("SMT Chic", "SMT Chacc"),
    ("SMT 邦典", "SMT 新邦"),
    ("SMT邦典2", "SMT新邦2"),
    ("SMT钟表匠2", "SMT表匠人"),
    ("SMT钟表匠", "SMT表大匠"),
    ("TM亨帝利", "TMxxx大利"),
    ("SMT卓磊", "SMTzld"),
    ("SMT均思2", "SMTxxjs2"),
    ("SMT靓美莱", "SMT好美来"),
    ("SMT泰琴", "SMT泰国琴"),
    ("SMT欧恒", "SMT欧亚恒"),
    ("AL悠洋", "AL太洋"),
    ("PDD悠洋", "PDD大洋"),
    ("SMT英店", "SMT英子店"),
    ("JD卓磊", "JD卓时光"),
    ("TM卓磊", "TM卓时尚"),
    ("SMT金冠", "SMT金版冠"),
    ("TM悠洋", "TM大洋"),
])

SHORT_SHOP_MAP = OrderedDict([
    ("亨帝利", "xxx大利"),
    ("卓磊", "zld"),
    ("悠洋", "大洋"),
    ("泰琴", "泰国琴"),
    ("靓美莱", "好美来"),
    ("均思2", "xxjs2"),
    ("欧恒", "欧亚恒"),
    ("钟表匠", "表大匠"),
    ("邦典2", "新邦2"),
    ("邦典", "新邦"),
    ("Arita", "Arlic"),
    ("Chic", "Chacc"),
    ("T-Strap", "T-Stp"),
    ("X-Wrist", "X-Wroit"),
])

DEFAULT_NAV = [
    {"name": "工作总览", "group": "总览", "view": "home", "table": "", "sort": 10, "enabled": True},
    {"name": "店铺管理", "group": "经营管理", "view": "store", "table": "店铺", "sort": 20, "enabled": True},
    {"name": "商品中心", "group": "经营管理", "view": "product", "table": "商品中心", "sort": 30, "enabled": True},
    {"name": "订单售后", "group": "经营管理", "view": "order", "table": "订单中心", "sort": 40, "enabled": True},
    {"name": "推广活动", "group": "经营管理", "view": "promo", "table": "推广活动", "sort": 50, "enabled": True},
    {"name": "广告管理", "group": "经营管理", "view": "admgmt", "table": "广告投放日报", "sort": 60, "enabled": True},
    {"name": "知识素材库", "group": "经营管理", "view": "know", "table": "知识素材库", "sort": 70, "enabled": True},
    {"name": "客户管理", "group": "经营管理", "view": "customer", "table": "客户管理", "sort": 80, "enabled": True},
    {"name": "单据制作", "group": "经营管理", "view": "doc", "table": "单据制作", "sort": 90, "enabled": True},
    {"name": "系统设置", "group": "系统", "view": "settings", "table": "工作台设置", "sort": 100, "enabled": True},
]

_token: str | None = None
_token_exp = 0.0
_table_ids: dict[str, str] = {}
_cache: dict[str, Any] = {"ts": 0.0, "payload": None}

app = FastAPI(title="OPC Workbench Live")


def remap_text(s: Any) -> str:
    if s is None:
        return ""
    out = str(s)
    for old, new in SHOP_MAP.items():
        if old in out:
            out = out.replace(old, new)
    for old, new in SHORT_SHOP_MAP.items():
        if old in out:
            out = out.replace(old, new)
    for old, new in MANAGER_MAP.items():
        if old in out:
            out = out.replace(old, new)
    return out


def cell(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, list):
        parts = []
        for x in v:
            if isinstance(x, dict):
                parts.append(x.get("text") or x.get("name") or str(x))
            else:
                parts.append(str(x))
        return remap_text("".join(parts) if len(parts) == 1 else ",".join(parts))
    if isinstance(v, dict):
        if "text" in v:
            return remap_text(v.get("text"))
        if "name" in v:
            return remap_text(v.get("name"))
        if "value" in v:
            return cell(v.get("value"))
        return remap_text(str(v))
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        # Feishu date as ms epoch
        if v > 10_000_000_000:
            try:
                dt = datetime.fromtimestamp(v / 1000, tz=timezone.utc).astimezone(TZ_SH)
                return dt.strftime("%Y/%m/%d")
            except Exception:
                return v
        return v
    return remap_text(v)


def num(v: Any, default: float = 0.0) -> float:
    if v is None or v == "":
        return default
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).replace(",", "").strip())
    except Exception:
        return default


def truthy_enabled(v: Any) -> bool:
    s = str(cell(v) or "").strip().lower()
    if s in ("否", "no", "n", "false", "0", "停用", "关", "禁用"):
        return False
    if s in ("", "是", "yes", "y", "true", "1", "启用", "开"):
        return True
    return True


def load_secret_fallback() -> str:
    global APP_SECRET
    if APP_SECRET:
        return APP_SECRET
    candidates = [
        Path("/home/box/agent-data/agents/99cb373b-0b6a-4900-98e5-6464cecbb45f/xiaofu_feishu_app_secret.txt"),
        Path("/etc/secrets/FEISHU_APP_SECRET"),
        Path("/etc/secrets/xiaofu_feishu_app_secret.txt"),
        Path(__file__).resolve().parent / ".feishu_secret",
    ]
    for p in candidates:
        if p.is_file():
            APP_SECRET = p.read_text(encoding="utf-8").strip()
            break
    return APP_SECRET


async def tenant_token(client: httpx.AsyncClient) -> str:
    global _token, _token_exp
    now = time.time()
    if _token and now < _token_exp - 60:
        return _token
    secret = load_secret_fallback()
    if not secret:
        raise RuntimeError("FEISHU_APP_SECRET missing")
    r = await client.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": secret},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 0:
        raise RuntimeError(f"feishu token error: {data.get('msg')}")
    _token = data["tenant_access_token"]
    _token_exp = now + int(data.get("expire", 7200))
    return _token


async def list_tables(client: httpx.AsyncClient, token: str) -> dict[str, str]:
    global _table_ids
    if _table_ids:
        return _table_ids
    items = []
    page_token = ""
    while True:
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BITABLE}/tables?page_size=100"
        if page_token:
            url += f"&page_token={page_token}"
        r = await client.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
        r.raise_for_status()
        data = r.json()
        if data.get("code") != 0:
            raise RuntimeError(data.get("msg"))
        items.extend(data.get("data", {}).get("items") or [])
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"]["page_token"]
    _table_ids = {i["name"]: i["table_id"] for i in items}
    return _table_ids


async def fetch_records(client: httpx.AsyncClient, token: str, table_id: str) -> list[dict]:
    out: list[dict] = []
    page_token = ""
    while True:
        url = (
            f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BITABLE}/tables/"
            f"{table_id}/records?page_size=500"
        )
        if page_token:
            url += f"&page_token={page_token}"
        r = await client.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=60)
        r.raise_for_status()
        data = r.json()
        if data.get("code") != 0:
            raise RuntimeError(data.get("msg"))
        out.extend(data.get("data", {}).get("items") or [])
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"]["page_token"]
    return out


def fields(rec: dict) -> dict:
    return rec.get("fields") or {}


def parse_nav(rows: list[dict]) -> list[dict]:
    items = []
    for rec in rows:
        f = fields(rec)
        name = cell(f.get("名称")) or ""
        if not name:
            continue
        enabled_raw = f.get("启用")
        enabled = True if enabled_raw is None else truthy_enabled(enabled_raw)
        items.append({
            "name": name,
            "group": cell(f.get("分组")) or "经营管理",
            "view": cell(f.get("视图标识")) or "custom",
            "table": cell(f.get("关联表名")) or "",
            "sort": int(num(f.get("排序"), 999)),
            "enabled": enabled,
        })
    items.sort(key=lambda x: (x["sort"], x["name"]))
    return [i for i in items if i["enabled"]]


def build_platforms(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        name = cell(f.get("平台名称"))
        if not name:
            continue
        out.append({
            "name": name,
            "code": cell(f.get("平台代码")) or "",
            "color": cell(f.get("Logo颜色")) or "#64748b",
            "status": cell(f.get("状态")) or "启用",
        })
    return out


def build_stores(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        name = cell(f.get("店铺名称"))
        if not name:
            continue
        out.append({
            "name": name,
            "platform": cell(f.get("平台名称")) or "",
            "manager": cell(f.get("经理")) or "",
            "status": "营业中",
            "type": "",
            "link": cell(f.get("后台链接")) or None,
            "yearly": num(f.get("2026年度营业额")),
            "monthly": num(f.get("本月营业额")),
            "latest": num(f.get("最新一天营业额")),
        })
    return out


def build_managers(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        name = cell(f.get("姓名"))
        if not name:
            continue
        out.append({
            "name": name,
            "status": cell(f.get("状态")) or "在职",
            "platform": cell(f.get("负责平台")) or "",
            "phone": cell(f.get("手机")) or "",
        })
    return out


def build_quick_links(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        name = cell(f.get("名称"))
        if not name:
            continue
        url = cell(f.get("网址")) or ""
        if "coze.site" in url.lower():
            url = "/"
        out.append({"name": name, "url": url, "desc": cell(f.get("说明")) or ""})
    return out


def build_settings(rows: list[dict]) -> dict:
    if not rows:
        return {"owner": "张三", "phone": "", "note": ""}
    f = fields(rows[0])
    return {
        "owner": cell(f.get("负责人")) or "张三",
        "phone": cell(f.get("联系电话")) or "",
        "note": cell(f.get("备注")) or "",
    }


def build_products(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "id": cell(f.get("商品编号")) or "",
            "name": cell(f.get("商品名称")) or "",
            "store": cell(f.get("所属店铺")) or "",
            "plat": cell(f.get("平台")) or "",
            "price": num(f.get("售价")),
            "stock": int(num(f.get("库存"))),
            "s30": int(num(f.get("近30天销量"))),
            "rating": num(f.get("评分")),
            "status": cell(f.get("状态")) or "",
        })
    return out


def build_orders(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "id": cell(f.get("订单号")) or "",
            "date": cell(f.get("下单日期")) or "",
            "store": cell(f.get("所属店铺")) or "",
            "plat": cell(f.get("平台")) or "",
            "product": cell(f.get("商品名称")) or "",
            "qty": int(num(f.get("数量"))),
            "amount": num(f.get("订单金额")),
            "buyer": cell(f.get("买家地区")) or "",
            "status": cell(f.get("订单状态")) or "",
        })
    return out


def build_aftersales(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "id": cell(f.get("工单号")) or "",
            "order": cell(f.get("关联订单")) or "",
            "date": cell(f.get("申请日期")) or "",
            "store": cell(f.get("所属店铺")) or "",
            "plat": cell(f.get("平台")) or "",
            "type": cell(f.get("售后类型")) or "",
            "reason": cell(f.get("申请原因")) or "",
            "amount": num(f.get("退款金额")),
            "status": cell(f.get("工单状态")) or "",
        })
    return out


def build_campaigns(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "name": cell(f.get("活动名称")) or "",
            "plat": cell(f.get("平台")) or "",
            "store": cell(f.get("适用店铺")) or "",
            "type": cell(f.get("活动类型")) or "",
            "start": cell(f.get("开始日期")) or "",
            "end": cell(f.get("结束日期")) or "",
            "budget": num(f.get("活动预算")),
            "spent": num(f.get("已花费")),
            "sales": num(f.get("带来成交")),
            "roi": num(f.get("ROI")),
            "status": cell(f.get("活动状态")) or "",
        })
    return out


def build_materials(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "name": cell(f.get("素材名称")) or "",
            "type": cell(f.get("素材类型")) or "",
            "size": cell(f.get("素材数量")) or "",
            "owner": cell(f.get("归属")) or "",
            "updated": cell(f.get("更新日期")) or "",
            "status": cell(f.get("状态")) or "",
        })
    return out


def build_ad_daily(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "date": cell(f.get("日期")) or "",
            "plat": cell(f.get("平台")) or "",
            "spend": num(f.get("广告花费")),
            "clicks": int(num(f.get("点击量"))),
            "sales": num(f.get("成交金额")),
            "roi": num(f.get("ROI")),
        })
    return out


def build_todos(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        done = f.get("完成")
        if isinstance(done, bool):
            is_done = done
        else:
            is_done = str(done).lower() in ("true", "1", "是")
        out.append({
            "title": cell(f.get("事项标题")) or "",
            "level": cell(f.get("紧急程度")) or "普通",
            "desc": cell(f.get("事项说明")) or "",
            "due": cell(f.get("截止时间")) or "",
            "plat": cell(f.get("涉及平台")) or "ALL",
            "done": is_done,
        })
    return out


def build_customers(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "id": cell(f.get("客户编号")) or "",
            "name": cell(f.get("客户名称")) or "",
            "type": cell(f.get("客户类型")) or "",
            "contact": cell(f.get("联系人")) or "",
            "region": cell(f.get("国家/地区")) or "",
            "plat": cell(f.get("来源平台")) or "",
            "orders": int(num(f.get("累计订单"))),
            "amount": num(f.get("累计金额")),
            "last": cell(f.get("最近下单日期")) or "",
            "level": cell(f.get("客户等级")) or "",
            "status": cell(f.get("客户状态")) or "",
        })
    return out


def build_documents(rows: list[dict]) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        out.append({
            "id": cell(f.get("单据编号")) or "",
            "type": cell(f.get("单据类型")) or "",
            "title": cell(f.get("单据标题")) or "",
            "customer": cell(f.get("关联客户")) or "",
            "amount": num(f.get("单据金额")),
            "maker": cell(f.get("制单人")) or "",
            "date": cell(f.get("制单日期")) or "",
            "status": cell(f.get("单据状态")) or "",
        })
    return out


def build_ad_requests(rows: list[dict], applicant: str) -> list[dict]:
    out = []
    for rec in rows:
        f = fields(rec)
        # flexible field names across the 3 tables
        title = cell(f.get("申请标题") or f.get("标题") or f.get("活动名称") or f.get("申请事由"))
        out.append({
            "id": cell(f.get("申请编号") or f.get("编号") or ""),
            "title": title or "广告费申请",
            "plat": cell(f.get("平台") or f.get("投放平台") or ""),
            "store": cell(f.get("店铺") or f.get("所属店铺") or ""),
            "amount": num(f.get("申请金额") or f.get("金额") or f.get("预算")),
            "reason": cell(f.get("申请原因") or f.get("事由") or f.get("备注") or ""),
            "applicant": applicant,
            "date": cell(f.get("申请日期") or f.get("日期") or ""),
            "dateStart": cell(f.get("开始日期") or ""),
            "dateEnd": cell(f.get("结束日期") or ""),
            "status": cell(f.get("状态") or f.get("审批状态") or "审批中"),
        })
    return out


def unpivot_sales(rows: list[dict], manager: str, store_meta: dict[str, dict]) -> list[dict]:
    skip = {"日期", "当天总金额", "合计", "总计"}
    daily = []
    for rec in rows:
        f = fields(rec)
        date_raw = f.get("日期")
        date_s = cell(date_raw)
        if not date_s:
            continue
        # normalize to YYYY/MM/DD
        if isinstance(date_raw, (int, float)) and date_raw > 10_000_000_000:
            dt = datetime.fromtimestamp(date_raw / 1000, tz=timezone.utc).astimezone(TZ_SH)
            date_s = dt.strftime("%Y/%m/%d")
        elif "-" in str(date_s):
            date_s = str(date_s).replace("-", "/")[:10]
        for k, v in f.items():
            if k in skip:
                continue
            sales = num(v)
            if sales == 0 and (v is None or v == ""):
                continue
            store = remap_text(k)
            meta = store_meta.get(store) or {}
            daily.append({
                "date": date_s,
                "store": store,
                "platform": meta.get("platform") or "",
                "manager": manager,
                "sales": sales,
                "orders": 0,
            })
    return daily


def summarize(daily: list[dict], stores: list[dict], year: str = "2026") -> dict:
    by_store: dict[str, dict] = {}
    by_platform: dict[str, dict] = {}
    by_manager: dict[str, dict] = {}
    dates = sorted({r["date"] for r in daily})
    latest_date = dates[-1] if dates else ""
    prev_date = dates[-2] if len(dates) >= 2 else ""
    # month of latest
    month_prefix = "/".join(latest_date.split("/")[:2]) if latest_date else ""

    for st in stores:
        by_store[st["name"]] = {
            "store": st["name"],
            "platform": st["platform"],
            "manager": st["manager"],
            "yearly": float(st.get("yearly") or 0),
            "monthly": float(st.get("monthly") or 0),
            "latest": float(st.get("latest") or 0),
        }

    for r in daily:
        st = by_store.setdefault(r["store"], {
            "store": r["store"], "platform": r["platform"], "manager": r["manager"],
            "yearly": 0.0, "monthly": 0.0, "latest": 0.0,
        })
        if not st.get("platform"):
            st["platform"] = r["platform"]
        if not st.get("manager"):
            st["manager"] = r["manager"]
        # Prefer Feishu store yearly/monthly if present; else accumulate
        # Only accumulate if store table didn't provide yearly
        # Always recompute latest from daily for consistency
        if r["date"] == latest_date:
            st["latest"] = st.get("latest") or 0
            # if store table had latest use max of both later
        if month_prefix and r["date"].startswith(month_prefix):
            pass

    # recompute yearly/monthly/latest from daily when store table numbers missing
    for name, st in by_store.items():
        rows = [r for r in daily if r["store"] == name]
        if not rows:
            continue
        yearly = sum(r["sales"] for r in rows if r["date"].startswith(year))
        monthly = sum(r["sales"] for r in rows if month_prefix and r["date"].startswith(month_prefix))
        latest = sum(r["sales"] for r in rows if r["date"] == latest_date)
        # Prefer larger of table vs computed (table may be authoritative)
        st["yearly"] = max(float(st.get("yearly") or 0), yearly) if st.get("yearly") else yearly
        if not st.get("yearly"):
            st["yearly"] = yearly
        # Actually: if store table had values use them; else computed
        # Simpler: always use computed from daily for consistency with trend
        st["yearly"] = yearly if yearly else float(st.get("yearly") or 0)
        st["monthly"] = monthly if monthly else float(st.get("monthly") or 0)
        st["latest"] = latest if latest else float(st.get("latest") or 0)

    # But store table already has remapped yearly - prefer store table when daily empty for that store
    for st0 in stores:
        st = by_store.get(st0["name"])
        if not st:
            continue
        if st["yearly"] == 0 and st0.get("yearly"):
            st["yearly"] = float(st0["yearly"])
        if st["monthly"] == 0 and st0.get("monthly"):
            st["monthly"] = float(st0["monthly"])
        if st["latest"] == 0 and st0.get("latest"):
            st["latest"] = float(st0["latest"])

    for st in by_store.values():
        p = st["platform"] or "未分配"
        bp = by_platform.setdefault(p, {"platform": p, "yearly": 0.0, "monthly": 0.0, "latest": 0.0, "stores": 0})
        bp["yearly"] += st["yearly"]
        bp["monthly"] += st["monthly"]
        bp["latest"] += st["latest"]
        bp["stores"] += 1
        m = st["manager"] or "未分配"
        bm = by_manager.setdefault(m, {"manager": m, "yearly": 0.0, "monthly": 0.0, "latest": 0.0})
        bm["yearly"] += st["yearly"]
        bm["monthly"] += st["monthly"]
        bm["latest"] += st["latest"]

    latest_total = sum(r["sales"] for r in daily if r["date"] == latest_date)
    prev_total = sum(r["sales"] for r in daily if r["date"] == prev_date)
    dod = ((latest_total - prev_total) / prev_total) if prev_total else 0.0
    yearly_total = sum(st["yearly"] for st in by_store.values())
    monthly_total = sum(st["monthly"] for st in by_store.values())

    trend_map: dict[str, float] = {}
    for r in daily:
        trend_map[r["date"]] = trend_map.get(r["date"], 0.0) + r["sales"]
    trend = [{"date": d, "total": trend_map[d]} for d in sorted(trend_map)]

    return {
        "summary": {
            "yearly_total": yearly_total,
            "monthly_total": monthly_total,
            "monthly_range": month_prefix.replace("/", "-") if month_prefix else "",
            "latest_total": latest_total,
            "latest_date": latest_date,
            "dod": dod,
            "prev_date": prev_date,
            "prev_total": prev_total,
            "by_store": list(by_store.values()),
            "by_platform": list(by_platform.values()),
            "by_manager": list(by_manager.values()),
        },
        "trend": trend,
        "data_range": {
            "from": dates[0] if dates else "",
            "to": dates[-1] if dates else "",
            "days": len(dates),
        },
    }


async def build_payload(client: httpx.AsyncClient) -> dict:
    token = await tenant_token(client)
    names = await list_tables(client, token)

    async def rows(key: str) -> list[dict]:
        tname = TABLES[key]
        tid = names.get(tname)
        if not tid:
            return []
        return await fetch_records(client, token, tid)

    platforms = build_platforms(await rows("platforms"))
    stores = build_stores(await rows("stores"))
    managers = build_managers(await rows("managers"))
    quick_links = build_quick_links(await rows("quick_links"))
    settings = build_settings(await rows("settings"))
    products = build_products(await rows("products"))
    orders = build_orders(await rows("orders"))
    aftersales = build_aftersales(await rows("aftersales"))
    campaigns = build_campaigns(await rows("campaigns"))
    materials = build_materials(await rows("materials"))
    ad_daily = build_ad_daily(await rows("ad_daily"))
    todos = build_todos(await rows("todos"))
    customers = build_customers(await rows("customers"))
    documents = build_documents(await rows("documents"))

    nav_rows = await rows("nav")
    nav_menu = parse_nav(nav_rows) if nav_rows else list(DEFAULT_NAV)
    nav_source = "feishu" if nav_rows else "default"

    store_meta = {s["name"]: s for s in stores}
    daily: list[dict] = []
    for key, mgr in MANAGER_FOR_SALES.items():
        daily.extend(unpivot_sales(await rows(key), mgr, store_meta))

    ad_requests: list[dict] = []
    for key, mgr in [("adreq_zhang", "张三"), ("adreq_li", "李四"), ("adreq_wang", "王五")]:
        ad_requests.extend(build_ad_requests(await rows(key), mgr))

    stats = summarize(daily, stores)
    now = datetime.now(TZ_SH).isoformat(timespec="seconds")

    # module bundle for frontend MOCK replacement
    modules = {
        "products": products,
        "orders": orders,
        "aftersales": aftersales,
        "campaigns": campaigns,
        "materials": materials,
        "adDaily": [
            {"date": x["date"], "plat": x["plat"], "spend": x["spend"], "clicks": x["clicks"],
             "gmv": x["sales"], "roi": x["roi"]}
            for x in ad_daily
        ],
        "todos": [
            {"title": t["title"], "level": t["level"], "desc": t["desc"], "due": t["due"],
             "plat": t["plat"], "done": t["done"]}
            for t in todos
        ],
        "customers": customers,
        "documents": documents,
        "adRequests": ad_requests,
        "refunds": [
            {"id": a["id"], "plat": a["plat"], "amount": a["amount"], "status": a["status"],
             "date": a["date"], "store": a["store"]}
            for a in aftersales if a.get("amount")
        ],
    }

    return {
        "updated_at": now,
        "yearly_year": "2026",
        "data_range": stats["data_range"],
        "summary": stats["summary"],
        "platforms": platforms,
        "stores": [{"name": s["name"], "platform": s["platform"], "manager": s["manager"],
                    "status": s["status"], "type": s["type"], "link": s["link"]} for s in stores],
        "managers": managers,
        "daily": daily,
        "trend": stats["trend"],
        "quick_links": quick_links,
        "settings": settings,
        "nav_menu": nav_menu,
        "nav_source": nav_source,
        "modules": modules,
        "source": "feishu",
    }


@app.get("/api/health")
async def health():
    return {
        "ok": True,
        "app_id": APP_ID,
        "bitable": BITABLE,
        "cache_ttl": CACHE_TTL,
        "has_secret": bool(load_secret_fallback()),
        "time": datetime.now(TZ_SH).isoformat(timespec="seconds"),
    }


@app.get("/api/data")
async def api_data(t: str | None = Query(None), refresh: int = Query(0)):
    global _cache, _table_ids
    now = time.time()
    if refresh:
        _cache = {"ts": 0.0, "payload": None}
        _table_ids = {}
    if _cache["payload"] and (now - _cache["ts"]) < CACHE_TTL and not refresh:
        return JSONResponse(_cache["payload"], headers={"Cache-Control": "no-store"})
    try:
        async with httpx.AsyncClient() as client:
            payload = await build_payload(client)
        _cache = {"ts": now, "payload": payload}
        return JSONResponse(payload, headers={"Cache-Control": "no-store"})
    except Exception as e:
        if _cache["payload"]:
            stale = dict(_cache["payload"])
            stale["warning"] = f"feishu_error:{type(e).__name__}"
            return JSONResponse(stale, headers={"Cache-Control": "no-store"})
        return JSONResponse({"error": str(e), "updated_at": datetime.now(TZ_SH).isoformat()}, status_code=502)


@app.get("/")
async def index():
    index_path = STATIC_DIR / "index.html"
    if not index_path.is_file():
        return JSONResponse({"error": "index.html missing"}, status_code=404)
    return FileResponse(index_path, media_type="text/html; charset=utf-8")


if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
