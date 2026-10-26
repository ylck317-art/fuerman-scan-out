/* ============================================================
 * 虚拟演示数据（MOCK）
 * 说明：当前商品/订单/售后/推广/素材/利润/退款/待办全部为演示数据，
 *       后续在飞书多维表建好对应表后，脚本把真实数据写入 data.json，
 *       网页自动替换，无需改动页面结构。
 * ============================================================ */
window.MOCK = {
  meta:{
    latestDate:'2026-10-08',
    generated:'2026-10-11',
    note:'全部为虚拟演示数据，可随时删除或替换'
  },

  /* ---------- 商品 ---------- */
  products:[
    {id:'P01', name:'苹果硅胶运动表带 45mm', store:'SMTzld', plat:'速卖通', price:39,  stock:860,  s30:426, rating:4.80, status:'在售'},
    {id:'P02', name:'苹果硅胶运动表带 49mm(Ultra)', store:'SMTzld', plat:'速卖通', price:45,  stock:320,  s30:358, rating:4.82, status:'在售'},
    {id:'P03', name:'米兰尼斯磁吸不锈钢表带', store:'SMT泰国琴', plat:'速卖通', price:98,  stock:145,  s30:289, rating:4.70, status:'在售'},
    {id:'P04', name:'真皮蝴蝶扣商务表带', store:'SMT泰国琴', plat:'速卖通', price:156, stock:62,   s30:168, rating:4.76, status:'在售'},
    {id:'P05', name:'尼龙回环魔术贴表带', store:'SMTxxjs2', plat:'速卖通', price:45,  stock:28,   s30:212, rating:4.68, status:'在售'},
    {id:'P06', name:'钛合金三珠金属表带', store:'SMT TOP Acso', plat:'速卖通', price:189, stock:84, s30:96, rating:4.90, status:'在售'},
    {id:'P07', name:'树脂果冻透明表带', store:'SMT好美来', plat:'速卖通', price:29,  stock:1240, s30:512, rating:4.62, status:'在售'},
    {id:'P08', name:'帆布编织户外表带', store:'SMTxxjs2', plat:'速卖通', price:69,  stock:76,   s30:88,  rating:4.71, status:'在售'},
    {id:'P09', name:'陶瓷镶钻女款表带', store:'TMxxx大利', plat:'天猫', price:168, stock:12,   s30:45,  rating:4.85, status:'补货中'},
    {id:'P10', name:'氟橡胶潜水表带', store:'SMTArlic 3c', plat:'速卖通', price:88, stock:430, s30:178, rating:4.79, status:'在售'},
    {id:'P11', name:'链式精钢表带', store:'SMT泰国琴', plat:'速卖通', price:129, stock:96,   s30:134, rating:4.74, status:'在售'},
    {id:'P12', name:'野径回环双节表带', store:'SMTzld', plat:'速卖通', price:59,  stock:510,  s30:268, rating:4.83, status:'在售'},
    {id:'P13', name:'高山回环表带', store:'SMT欧亚恒', plat:'速卖通', price:55,  stock:380,  s30:202, rating:4.80, status:'在售'},
    {id:'P14', name:'海洋双扣表带', store:'SMT欧亚恒', plat:'速卖通', price:69,  stock:14,   s30:156, rating:4.77, status:'在售'},
    {id:'P15', name:'小牛皮手工缝线表带', store:'AL太洋', plat:'阿里巴巴', price:128, stock:260, s30:64, rating:4.66, status:'在售'},
    {id:'P16', name:'碳纤维纹理表带', store:'SMT欧亚恒', plat:'速卖通', price:109, stock:210,  s30:92,  rating:4.88, status:'在售'},
    {id:'P17', name:'弹力编织单圈表带', store:'SMT好美来', plat:'速卖通', price:49, stock:680, s30:318, rating:4.70, status:'在售'},
    {id:'P18', name:'华为GT4硅胶表带', store:'PDD大洋', plat:'拼多多', price:29, stock:8,    s30:188, rating:4.65, status:'补货中'}
  ],

  /* ---------- 订单 ---------- */
  orders:[
    {id:'SO26100801', date:'2026-10-08', store:'SMTzld',        plat:'速卖通', product:'苹果硅胶运动表带 45mm', qty:2, amount:78,  buyer:'美国',   status:'待发货'},
    {id:'SO26100802', date:'2026-10-08', store:'SMT泰国琴',        plat:'速卖通', product:'米兰尼斯磁吸表带',      qty:1, amount:98,  buyer:'西班牙', status:'待发货'},
    {id:'SO26100803', date:'2026-10-08', store:'SMTxxjs2',       plat:'速卖通', product:'真皮蝴蝶扣表带',        qty:1, amount:156, buyer:'巴西',   status:'已发货'},
    {id:'SO26100804', date:'2026-10-08', store:'SMT欧亚恒',        plat:'速卖通', product:'尼龙回环表带',          qty:3, amount:135, buyer:'俄罗斯', status:'待发货'},
    {id:'SO26100805', date:'2026-10-08', store:'SMT TOP Acso', plat:'速卖通', product:'钛合金三珠表带',     qty:1, amount:189, buyer:'美国',   status:'待发货'},
    {id:'SO26100806', date:'2026-10-08', store:'SMT好美来',      plat:'速卖通', product:'树脂果冻表带',          qty:2, amount:58,  buyer:'美国',   status:'已发货'},
    {id:'SO26100701', date:'2026-10-07', store:'TMxxx大利',       plat:'天猫',   product:'陶瓷镶钻女款表带',      qty:1, amount:168, buyer:'浙江',   status:'待发货'},
    {id:'SO26100702', date:'2026-10-07', store:'SMTArlic 3c',    plat:'速卖通', product:'氟橡胶潜水表带',        qty:1, amount:88,  buyer:'德国',   status:'已发货'},
    {id:'SO26100703', date:'2026-10-07', store:'SMTzld',        plat:'速卖通', product:'硅胶运动表带',          qty:2, amount:78,  buyer:'俄罗斯', status:'已发货'},
    {id:'SO26100704', date:'2026-10-07', store:'PDD大洋',        plat:'拼多多', product:'华为GT4硅胶表带',       qty:1, amount:29,  buyer:'广东',   status:'待发货'},
    {id:'SO26100601', date:'2026-10-06', store:'SMT泰国琴',        plat:'速卖通', product:'链式精钢表带',          qty:1, amount:129, buyer:'英国',   status:'待发货'},
    {id:'SO26100602', date:'2026-10-06', store:'AL太洋',         plat:'阿里巴巴', product:'小牛皮手工缝线表带(批)', qty:10, amount:980, buyer:'福建', status:'待发货'},
    {id:'SO26100603', date:'2026-10-06', store:'SMTxxjs2',       plat:'速卖通', product:'帆布编织表带',          qty:1, amount:69,  buyer:'法国',   status:'已完成'},
    {id:'SO26100604', date:'2026-10-06', store:'SMT欧亚恒',        plat:'速卖通', product:'碳纤维纹理表带',        qty:1, amount:109, buyer:'日本',   status:'待付款'}
  ],

  /* ---------- 售后工单 ---------- */
  aftersales:[
    {id:'AF2026100501', order:'SO26100507', date:'2026-10-05', store:'TMxxx大利',  plat:'天猫',   type:'退货退款', reason:'尺寸不符',       amount:420, status:'待处理'},
    {id:'AF2026100201', order:'SO26092812', date:'2026-10-02', store:'SMTzld',  plat:'速卖通', type:'仅退款',   reason:'表带褪色',       amount:268, status:'已完成'},
    {id:'AF2026100301', order:'SO26093003', date:'2026-10-03', store:'SMT泰国琴',  plat:'速卖通', type:'换货',     reason:'表带太长需换短款', amount:159, status:'处理中'},
    {id:'AF2026100502', order:'SO26100208', date:'2026-10-05', store:'SMT欧亚恒',  plat:'速卖通', type:'仅退款',   reason:'运输中包装损坏',  amount:89,  status:'处理中'},
    {id:'AF2026100601', order:'SO26100104', date:'2026-10-06', store:'PDD大洋',  plat:'拼多多', type:'退货退款', reason:'商品与描述不符',  amount:126, status:'已完成'},
    {id:'AF2026100701', order:'SO26100402', date:'2026-10-07', store:'SMT好美来',plat:'速卖通', type:'仅退款',   reason:'缺货协商退款',    amount:520, status:'已完成'},
    {id:'AF2026100702', order:'SO26100506', date:'2026-10-07', store:'SMTxxjs2', plat:'速卖通', type:'维修',     reason:'表扣松动',        amount:0,   status:'处理中'},
    {id:'AF2026100801', order:'SO26100309', date:'2026-10-08', store:'AL太洋',   plat:'阿里巴巴', type:'仅退款', reason:'协商退款',        amount:360, status:'待处理'}
  ],

  /* ---------- 推广活动 ---------- */
  campaigns:[
    {name:'速卖通双11大促预热', plat:'速卖通', store:'全部店铺', type:'平台大促',   start:'2026-10-08', end:'2026-11-11', budget:120000, spent:18600, sales:72400,  roi:3.90, status:'进行中'},
    {name:'秋冬款直通车关键词', plat:'速卖通', store:'全部店铺', type:'搜索广告',   start:'2026-09-20', end:'2026-10-31', budget:30000,  spent:22400, sales:86200,  roi:3.85, status:'进行中'},
    {name:'天猫秋冬上新',       plat:'天猫',   store:'TMxxx大利', type:'店铺活动',   start:'2026-10-01', end:'2026-10-20', budget:15000,  spent:6200,  sales:18400,  roi:2.97, status:'进行中'},
    {name:'硅胶款限时折扣',     plat:'速卖通', store:'SMT好美来', type:'折扣促销',  start:'2026-10-05', end:'2026-10-12', budget:8000,   spent:3600,  sales:11200,  roi:3.11, status:'进行中'},
    {name:'达人联盟带货',       plat:'速卖通', store:'全部店铺', type:'联盟营销',   start:'2026-09-01', end:'2026-12-31', budget:50000,  spent:28600, sales:124800, roi:4.36, status:'进行中'},
    {name:'多多搜索推广',       plat:'拼多多', store:'PDD大洋',  type:'搜索广告',   start:'2026-09-15', end:'2026-10-15', budget:6000,   spent:4200,  sales:9800,   roi:2.33, status:'已结束'},
    {name:'Ozon十月平台促销',   plat:'Ozon',   store:'全部店铺', type:'平台活动',   start:'2026-10-01', end:'2026-10-15', budget:20000,  spent:0,     sales:0,      roi:0,    status:'筹备中'}
  ],

  /* ---------- 素材库 ---------- */
  materials:[
    {name:'硅胶表带主图套装',     type:'主图',   size:'18 张', owner:'SMTzld', updated:'2026-10-08', status:'已发布'},
    {name:'米兰尼斯详情页',       type:'详情页', size:'1 份',  owner:'SMT泰国琴', updated:'2026-10-06', status:'待审核'},
    {name:'真皮表带实拍视频',     type:'视频',   size:'2 条',  owner:'SMTxxjs2', updated:'2026-10-05', status:'已发布'},
    {name:'客服标准回复话术',     type:'话术',   size:'1 份',  owner:'运营组',   updated:'2026-10-04', status:'已发布'},
    {name:'双11活动 Banner',      type:'主图',   size:'6 张',  owner:'设计组',   updated:'2026-10-07', status:'草稿'},
    {name:'表带尺寸测量教程',     type:'文档',   size:'1 份',  owner:'运营组',   updated:'2026-09-28', status:'已发布'},
    {name:'钛合金款开箱视频',     type:'视频',   size:'1 条',  owner:'SMT TOP',  updated:'2026-10-02', status:'待审核'},
    {name:'新品上架 SOP',         type:'文档',   size:'1 份',  owner:'运营组',   updated:'2026-09-25', status:'归档'},
    {name:'售后处理话术卡',       type:'话术',   size:'3 张',  owner:'客服组',   updated:'2026-10-03', status:'已发布'},
    {name:'氟橡胶详情长图',       type:'详情页', size:'1 份',  owner:'SMTArlic 3c', updated:'2026-09-30', status:'草稿'}
  ],

  /* ---------- 利润（月度） ---------- */
  finance:{
    monthly:[
      {month:'2026-05', revenue:642800, cost:385000, fee:58000, ad:27200,  profit:172600},
      {month:'2026-06', revenue:688400, cost:412000, fee:62500, ad:29800,  profit:184100},
      {month:'2026-07', revenue:726900, cost:431000, fee:66200, ad:32400,  profit:197300},
      {month:'2026-08', revenue:762300, cost:448000, fee:69800, ad:35600,  profit:208900},
      {month:'2026-09', revenue:812600, cost:476000, fee:74500, ad:38900,  profit:223200},
      {month:'2026-10', revenue:302400, cost:178500, fee:27800, ad:18420,  profit:77680}
    ],
    platformMonth:{'速卖通':70800,'天猫':4200,'阿里巴巴':1560,'拼多多':1120}
  },

  /* ---------- 退款明细 ---------- */
  refunds:[
    {id:'RF26100201', date:'2026-10-02', plat:'速卖通', store:'SMTzld',   amount:268, reason:'表带褪色',    status:'已完成'},
    {id:'RF26100301', date:'2026-10-03', plat:'速卖通', store:'SMT泰国琴',   amount:159, reason:'七天无理由',  status:'处理中'},
    {id:'RF26100501', date:'2026-10-05', plat:'天猫',   store:'TMxxx大利',  amount:420, reason:'尺寸不符',    status:'待处理'},
    {id:'RF26100502', date:'2026-10-05', plat:'速卖通', store:'SMT欧亚恒',   amount:89,  reason:'物流损坏',    status:'处理中'},
    {id:'RF26100601', date:'2026-10-06', plat:'拼多多', store:'PDD大洋',   amount:126, reason:'描述不符',    status:'已完成'},
    {id:'RF26100701', date:'2026-10-07', plat:'速卖通', store:'SMT好美来', amount:520, reason:'缺货退款',    status:'已完成'},
    {id:'RF26100702', date:'2026-10-07', plat:'速卖通', store:'SMTxxjs2',  amount:198, reason:'买错款式',    status:'处理中'},
    {id:'RF26100801', date:'2026-10-08', plat:'阿里巴巴', store:'AL太洋',  amount:360, reason:'协商退款',    status:'待处理'}
  ],

  /* ---------- 待办 ---------- */
  todos:[
    {level:'紧急', title:'12 笔订单即将超时未发货', desc:'需在今天 18:00 前完成揽收', due:'2026-10-08 18:00', plat:'ALL',    done:false},
    {level:'紧急', title:'TMxxx大利 ¥420 售后待处理', desc:'买家已等待 2 天，超时将影响评分', due:'2026-10-08 16:00', plat:'天猫', done:false},
    {level:'紧急', title:'3 款表带库存低于安全线', desc:'尼龙回环 / 海洋双扣 / 华为GT4', due:'2026-10-09 12:00', plat:'ALL', done:false},
    {level:'重要', title:'双11大促活动素材审核', desc:'Banner 6 张待设计组确认', due:'2026-10-10 18:00', plat:'ALL', done:false},
    {level:'重要', title:'直通车关键词调价', desc:'秋冬款 28 个关键词出价待优化', due:'2026-10-09 20:00', plat:'速卖通', done:false},
    {level:'重要', title:'9 月经营月报复盘', desc:'利润环比 +6.8%，需汇总下月计划', due:'2026-10-12 18:00', plat:'ALL', done:false},
    {level:'一般', title:'更新商品详情页卖点', desc:'补充 2026 新款材质说明', due:'2026-10-15 18:00', plat:'ALL', done:false},
    {level:'一般', title:'新人客服话术培训', desc:'售后处理话术卡 3 张已更新', due:'2026-10-16 18:00', plat:'ALL', done:false}
  ],

  /* ---------- AI 经营建议（虚拟演示） ---------- */
  suggestions:[
    {ic:'🔥', text:'硅胶运动表带近 7 天转化率最高（4.2%），建议双11备货增加 30%。'},
    {ic:'🎯', text:'SMT好美来广告 ROI 低于店铺均值，建议收缩宽泛词、转向精准长尾词。'},
    {ic:'📏', text:'退款多集中在“尺寸不符”，建议详情页顶部增加尺寸测量引导图。'}
  ],

  /* ---------- 行业新闻（AI 接入，演示版先内置；后续由脚本定时抓取替换） ---------- */
  news:[
    {cat:'policy', label:'政策', title:'七部门部署品质电商“五优”行动，双11等消费节点加强规范', src:'央视新闻', url:'http://m.toutiao.com/group/7694893093841093129/'},
    {cat:'plat',   label:'天猫', title:'今年双11取消跨店满减，统一官方立减，价格监测防“先涨后降”', src:'36氪', url:'https://36kr.com/p/40180****4807175'},
    {cat:'plat',   label:'速卖通', title:'年度峰会10月19日深圳举行，发布年度战略与双11政策', src:'出海网', url:'https://www.chwang.com/aliexpress/news'},
    {cat:'policy', label:'欧盟', title:'150欧元以下小包取消免税，11月再加2欧元处理费，直发模式承压', src:'36氪', url:'https://36kr.com/p/40170****5377033'},
    {cat:'watch',  label:'钟表', title:'德勤年度报告：瑞士钟表业适应“永久性较低销量”，转向结构性调整', src:'WATCHPRO', url:'https://www.watchpro.com/news/business-news/'},
    {cat:'ind',    label:'行业', title:'霍尔果斯前7月跨境电商贸易额184亿元，中亚市场持续高增长', src:'新华社', url:'http://m.toutiao.com/group/7694633681020846619/'}
  ],

  /* ---------- 业绩目标（演示版；后续可在飞书维护） ---------- */
  goals:{
    year:{target:8000000, done:4662247},
    month:{target:800000,  done:174088,   daysInMonth:31, daysPassed:8}
  },

  /* ---------- 客户管理（虚拟演示） ---------- */
  customers:[
    {id:'C001', name:'Green Essence', type:'批发商', contact:'Anna Nowak', country:'波兰',   plat:'速卖通', orders:64, amount:128600, lastOrder:'2026-10-06', level:'VIP',  status:'活跃'},
    {id:'C002', name:'TimeZone Retail', type:'零售商', contact:'Mark Lee',   country:'美国',   plat:'速卖通', orders:48, amount:86400,  lastOrder:'2026-10-05', level:'重要', status:'活跃'},
    {id:'C003', name:'表带工坊（广州）', type:'零售商', contact:'陈志远',     country:'中国',   plat:'阿里巴巴', orders:31, amount:24800,  lastOrder:'2026-09-29', level:'普通', status:'活跃'},
    {id:'C004', name:'Horloges BV', type:'批发商', contact:'Jeroen van Dijk', country:'荷兰', plat:'速卖通', orders:27, amount:52300,  lastOrder:'2026-09-25', level:'重要', status:'活跃'},
    {id:'C005', name:'PDD优品仓', type:'分销商', contact:'王佳',       country:'中国',   plat:'拼多多', orders:22, amount:11200,  lastOrder:'2026-09-20', level:'普通', status:'沉睡'},
    {id:'C006', name:'WatchParts DE', type:'批发商', contact:'Klaus Weber', country:'德国',   plat:'速卖通', orders:19, amount:41700,  lastOrder:'2026-08-30', level:'普通', status:'沉睡'},
    {id:'C007', name:'天猫xxx大利会员群', type:'零售商', contact:'李娜',     country:'中国',   plat:'天猫', orders:15, amount:9600,   lastOrder:'2026-10-08', level:'普通', status:'活跃'},
    {id:'C008', name:'Relojes Iberia', type:'分销商', contact:'Carlos Ruiz', country:'西班牙', plat:'速卖通', orders:12, amount:23800,  lastOrder:'2026-07-18', level:'普通', status:'流失'},
    {id:'C009', name:'Milan Straps Co', type:'零售商', contact:'Sara Conti', country:'意大利', plat:'速卖通', orders:9,  amount:17400,  lastOrder:'2026-10-02', level:'普通', status:'活跃'},
    {id:'C010', name:'智能穿戴配件店', type:'零售商', contact:'赵一鸣',     country:'中国',   plat:'阿里巴巴', orders:6,  amount:5200,   lastOrder:'2026-09-12', level:'普通', status:'新客'}
  ],

  /* ---------- 单据制作（虚拟演示） ---------- */
  documents:[
    {id:'DOC2026100801', type:'销售单', title:'表带销售单-Green Essence', customer:'Green Essence', amount:18600, maker:'张三', date:'2026-10-08', status:'已审核'},
    {id:'DOC2026100701', type:'销售单', title:'表带销售单-TimeZone Retail', customer:'TimeZone Retail', amount:9400,  maker:'张三', date:'2026-10-07', status:'已审核'},
    {id:'DOC2026100602', type:'报价单', title:'米兰尼斯表带报价-Horloges BV', customer:'Horloges BV', amount:0,     maker:'张三', date:'2026-10-06', status:'已发送'},
    {id:'DOC2026100601', type:'采购单', title:'硅胶原料采购单-东莞供应商', customer:'表带工坊（广州）', amount:26800, maker:'张三', date:'2026-10-06', status:'草稿'},
    {id:'DOC2026100501', type:'发货单', title:'订单批量发货单(美国线)', customer:'TimeZone Retail', amount:0,    maker:'张三', date:'2026-10-05', status:'已出库'},
    {id:'DOC2026100201', type:'销售单', title:'表带销售单-Milan Straps', customer:'Milan Straps Co', amount:7200,  maker:'张三', date:'2026-10-02', status:'已审核'},
    {id:'DOC2026092801', type:'对账单', title:'9月客户对账单-WatchParts', customer:'WatchParts DE', amount:41700, maker:'张三', date:'2026-09-28', status:'已确认'},
    {id:'DOC2026092001', type:'退货单', title:'退货入库单-PDD优品仓', customer:'PDD优品仓', amount:2300, maker:'张三', date:'2026-09-20', status:'已入库'}
  ],

  /* ---------- 广告管理 ---------- */
  adBudget:{
    lastMonthRevenue:812600,
    totalAdSpend:38900,
    totalAdSales:152400,
    monthlyBudget:50000,
    usedBudget:38900,
    pendingRequests:18000
  },
  adPlatformBudget:[
    {plat:'速卖通', budget:22000, spent:18600, sales:86200, roi:4.63, status:'正常'},
    {plat:'天猫',   budget:8000,  spent:5200,  sales:18400, roi:3.54, status:'正常'},
    {plat:'拼多多', budget:6000,  spent:4200,  sales:9800,  roi:2.33, status:'预警'},
    {plat:'Ozon',   budget:8000,  spent:3200,  sales:12800, roi:4.00, status:'正常'},
    {plat:'阿里巴巴',budget:4000, spent:2100,  sales:5600,  roi:2.67, status:'正常'},
    {plat:'京东',   budget:2000,  spent:800,   sales:2400,  roi:3.00, status:'正常'},
    {plat:'抖店',   budget:0,     spent:0,     sales:0,     roi:0,    status:'未开通'}
  ],
  adRequests:[
    {id:'AD2026100801', title:'双11大促广告预算申请',     plat:'速卖通', store:'全部店铺', amount:35000, reason:'双11大促期间流量激增，需加大直通车+联盟推广投入', applicant:'张三', date:'2026-10-08', dateStart:'2026-10-20', dateEnd:'2026-11-15', status:'审批中'},
    {id:'AD2026100601', title:'天猫秋冬新品推广费',       plat:'天猫',   store:'TMxxx大利', amount:8000,  reason:'秋冬新款上架，需搜索+推荐双渠道推广', applicant:'张三', date:'2026-10-06', dateStart:'2026-10-10', dateEnd:'2026-10-31', status:'已通过'},
    {id:'AD2026100501', title:'Ozon十月平台促销广告',     plat:'Ozon',   store:'全部店铺', amount:12000, reason:'Ozon平台十月大促，争取首页资源位', applicant:'张三', date:'2026-10-05', dateStart:'2026-10-08', dateEnd:'2026-10-20', status:'已通过'},
    {id:'AD2026100301', title:'拼多多搜索推广追加',       plat:'拼多多', store:'PDD大洋',  amount:3000,  reason:'现有ROI偏低，追加精准词测试', applicant:'张三', date:'2026-10-03', dateStart:'2026-10-05', dateEnd:'2026-10-25', status:'已驳回'},
    {id:'AD2026100101', title:'硅胶款限时折扣推广',       plat:'速卖通', store:'SMT好美来', amount:5000,  reason:'新品测试期，小预算验证转化率', applicant:'张三', date:'2026-10-01', dateStart:'2026-10-01', dateEnd:'2026-10-15', status:'已执行'},
    {id:'AD2026092801', title:'达人联盟Q4推广预算',       plat:'速卖通', store:'全部店铺', amount:20000, reason:'Q4达人带货联盟佣金+样品费用', applicant:'张三', date:'2026-09-28', dateStart:'2026-10-01', dateEnd:'2026-12-31', status:'已执行'},
    {id:'AD2026092501', title:'京东店铺开通推广',         plat:'京东',   store:'JD大洋',   amount:2000,  reason:'新店铺冷启动，测试京准通', applicant:'张三', date:'2026-09-25', dateStart:'2026-09-28', dateEnd:'2026-10-28', status:'已执行'},
    {id:'AD2026092001', title:'阿里巴巴国际站推广',       plat:'阿里巴巴',store:'AL太洋',  amount:4000,  reason:'B端客户开发，P4P+顶展', applicant:'张三', date:'2026-09-20', dateStart:'2026-09-22', dateEnd:'2026-10-22', status:'已执行'}
  ]
};

/* ---------- 生成近 14 天广告投放（确定性伪随机，日期与最新营业日对齐） ---------- */
(function(){
  function seedRand(seed){return function(){seed=(seed*9301+49297)%233280;return seed/233280;};}
  function addDays(s,n){
    const [Y,Mo,D]=s.split('-').map(Number);
    const d=new Date(Y,Mo-1,D+n);
    const p=x=>String(x).padStart(2,'0');
    return d.getFullYear()+'-'+p(d.getMonth()+1)+'-'+p(d.getDate());
  }
  const M=window.MOCK, rows=[];
  for(let i=13;i>=0;i--){
    const d=addDays(M.meta.latestDate,-i);
    const r=seedRand(42+i*7)();
    rows.push({date:d, plat:'速卖通', cost:Math.round(820+r*420), clicks:Math.round(180+r*120)});
    if(i<7){const r2=seedRand(99+i*5)();
      rows.push({date:d, plat:'天猫', cost:Math.round(150+r2*120), clicks:Math.round(40+r2*30)});}
    if(i<10){const r3=seedRand(7+i*11)();
      rows.push({date:d, plat:'拼多多', cost:Math.round(60+r3*60), clicks:Math.round(20+r3*25)});}
    if(i<3){const r4=seedRand(3+i*13)();
      rows.push({date:d, plat:'阿里巴巴', cost:Math.round(70+r4*50), clicks:Math.round(15+r4*15)});}
  }
  rows.forEach((x,i)=>{const rr=seedRand(7+i*3)();
    x.sales=Math.round(x.cost*(3.1+rr*1.9));});
  M.adDaily=rows;
})();
