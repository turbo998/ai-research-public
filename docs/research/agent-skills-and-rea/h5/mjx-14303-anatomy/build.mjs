import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "file:///C:/Users/qichen2/.copilot/skills/anatomy/kit/iso-kit.mjs";
import * as G from "file:///C:/Users/qichen2/.copilot/skills/anatomy/kit/lathe.mjs";
import { tubePieces, tubeSvg } from "file:///C:/Users/qichen2/.copilot/skills/anatomy/kit/tube.mjs";
import * as A from "file:///C:/Users/qichen2/.copilot/skills/anatomy/kit/audit.mjs";
import { kitScript } from "file:///C:/Users/qichen2/.copilot/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";
const runAudit = process.argv.includes("--audit");

const WIDTH = 960;
const HEIGHT = 610;

// World coordinate system:
// x: longitudinal axis (-142 front splitter -> +142 rear wing; 192 units wheelbase: front axle x = -84, rear axle x = +84)
// y: lateral axis (-64 left wheel -> +64 right wheel; 125 units track width)
// z: vertical axis (0 chassis bottom reference)
const BENCH = { x: -172, y: -106, w: 344, d: 212, r: 10 };
const BENCH_Z = -18;
const BENCH_H = 10;
const FOOT_H = 5;

const CHASSIS = { x: -118, y: -38, w: 236, d: 76, r: 10 };
const CHASSIS_Z = 2;
const CHASSIS_H = 5;

const AXLE_F = -84;
const AXLE_R = 84;
const TRACK_Y = 62;
const WHEEL_R = 26;
const WHEEL_W = 18;
const WHEEL_Z = 18;

const P = k.fitProjection(
  [
    ...k.boxCorners(BENCH, BENCH_Z - FOOT_H, 0),
    [-152, -86, 156],
    [152, 86, 156],
  ],
  WIDTH,
  HEIGHT,
  { pad: 22, azimuth: 41, elevation: 29 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);

// 12 Mechanical Sub-Assemblies of MJX Hyper Go 14303 (1/14 4WD Rally/Drift Complete Vehicle)
const PIECES = {
  chassis: {
    num: "01",
    name: "6061-T6 铝合金蜂窝底盘 & 防撞总成",
    en: "6061-T6 Alu Honeycomb Chassis & Bumpers",
    spec: "192 mm 轴距 · 2.0 mm 阳极氧化铝板 · EVA 吸能前杠 + LED 射灯 + 5 鳍片后扩散器",
    colorTag: "枪灰铝合金 + 活力橙前杠",
    principle:
      "整车承载基座。采用 6061-T6 铝合金 CNC 折弯成型并铣出蜂窝减重散热槽；前端配备宽体高吸能 EVA 海绵防撞、拉力前铲及双联高流明 LED 雾灯舱，尾部集成 5 通道文丘里下压力扩散器。",
    move: [0, 0, -16],
  },
  drivetrain: {
    num: "02",
    name: "4WD 中央金属主轴 & 前后行星伞齿差速器",
    en: "4WD Center Shaft & Planetary Bevel Diffs",
    spec: "FDR 8.54:1 · 15T/45T 钢齿 · 37T/13T 粉末冶金伞齿 + 4 星齿轮差速器",
    colorTag: "钛金主传动链 + 铬钢 CVD",
    principle:
      "【核心焦点总成】全时四驱刚性动力链：2845 无刷电机经 15T 钢制马达齿驱动 45T 金属主齿（初级减速 3.0:1），带动中央铝合金主轴与前后透明波箱内的 37T/13T 粉末冶金伞齿及 4 颗内部行星差速齿轮（次级减速 2.846:1），由铬钢 CVD 万向节分配至四轮。",
    move: [0, 0, 24],
  },
  motor: {
    num: "03",
    name: "2845 3700KV 四极无刷电机 & 涡轮散热甲",
    en: "2845 3700KV 4-Pole Brushless Motor & Fan",
    spec: "3700 KV · 2S 27,380 RPM / 3S 41,070 RPM · 6 环赤红散热鳍 + 6 叶高速风扇",
    colorTag: "钴蓝电机罐 + 阳极赤红散热鳍",
    principle:
      "中后置偏右布局的四极高扭无感无刷电机，外部套装 6 环阳极氧化赤红铝合金散热鳍片与顶部 14,000 RPM 六叶涡轮风扇；经黄/蓝/橙三相高柔硅胶线（U/V/W）输入高频换相电流，3S 下爆发 62.4 km/h 极速。",
    move: [20, 32, 42],
  },
  esc: {
    num: "04",
    name: "E45R 45A 无刷电调 & G3C 陀螺仪接收机",
    en: "45A Brushless ESC & G3C Gyro Receiver",
    spec: "45A 持续电流 · 双低压超容 · 内置 G3C 压电横摆陀螺仪 + 状态 LED",
    colorTag: "翡翠绿精密 PCB + 冰蓝散热排",
    principle:
      "防泼水 E45R 45A 独立无刷电调配备 7 片式散热排与双联滤波电容，抑制 3S 弹射起步电压跌落；独立接收机内置 G3C 压电陀螺仪，实时侦测车尾横摆角速度并向转向舵机注入毫秒级自动反打指令（Counter-steer）。",
    move: [-16, -36, 40],
  },
  battery: {
    num: "05",
    name: "2S/3S 高倍率锂电池仓 & XT60 供电总成",
    en: "2S 7.4V / 3S 11.1V LiPo Pack & XT60 Harness",
    spec: "7.4V 2000mAh / 11.1V 3S · 纵向配重仓 · XT60 主电源插头 + JST 平衡充线",
    colorTag: "深海蓝锂电包 + 琥珀黄 XT60",
    principle:
      "布置于底盘左侧纵向电池槽内，与右侧电机+舵机形成 50:50 左右动态横滚平衡；快拆防松桥式压板锁定，通过琥珀黄 XT60 大电流插头与多芯平衡头向电调输送峰值逾 90A 的瞬态电流。",
    move: [24, -42, 36],
  },
  servo: {
    num: "06",
    name: "17g 金属齿数字舵机 & 双摇臂阿克曼转向",
    en: "17g Digital Servo & Dual-Bellcrank Ackermann",
    spec: "2.4 kg·cm 扭矩 · 0.11s/60° · 弹簧舵机保 (Servo Saver) + 可调球头拉杆",
    colorTag: "钛灰舵机壳 + 玫瑰金转向桥",
    principle:
      "17g 高速数字舵机驱动铝合金双摇臂转向桥（Dual-Bellcrank）。主摇臂立柱内置高刚度缓冲弹簧（Servo Saver），在砂石飞跳或撞击路肩时吸收反向冲击；梯形几何连杆实现内轮大转角（1.08×）、外轮小转角（0.84×）的精准阿克曼差速转向。",
    move: [-20, 38, 38],
  },
  suspension_f: {
    num: "07",
    name: "前独立双叉臂悬架 & 油压绞牙金属避震",
    en: "Front Double-Wishbone & Oil-Filled Coilovers",
    spec: "赤红 CNC 前蝴蝶架 · 充油金属避震筒 · 滚花绞牙调节环 · 14 mm 行程",
    colorTag: "阳极赤红蝴蝶架 + 电光青避震筒",
    principle:
      "上下 A 臂独立悬架配合可调倾角拉杆，确保前轮大幅跳动时接地面积恒定；两支充油金属绞牙避震器锚定于赤红 CNC 铝合金前蝴蝶架，通过滚花预载环调节车头离地高度与入弯点头阻尼。",
    move: [-62, 0, 44],
  },
  suspension_r: {
    num: "08",
    name: "后独立双叉臂悬架 & 后油压绞牙金属避震",
    en: "Rear Double-Wishbone & Oil-Filled Coilovers",
    spec: "赤红 CNC 后蝴蝶架 · 渐进式螺旋弹簧 · 出弯抗下蹲支撑几何",
    colorTag: "阳极赤红蝴蝶架 + 电光青避震筒",
    principle:
      "后双叉臂悬架连接后差速器箱体与后轮座，后油压绞牙避震器针对 3S 狂暴动力调校了渐进式阻尼，抑制急加速车尾过度下蹲（Squat）并吸收飞跳落地冲击。",
    move: [62, 0, 44],
  },
  wheels_f: {
    num: "09",
    name: "前 58mm 拉力轮总成 & 通风刹车盘/红卡钳",
    en: "Front 58mm Rally Wheels & Brake Rotors/Calipers",
    spec: "Ø58 × 24 mm 人字拉力胎 · 6 辐金色轮毂 · 打孔通风刹车盘 + 赤红卡钳",
    colorTag: "香槟金 6 辐轮毂 + 赤红刹车卡钳",
    principle:
      "高抓地人字纹拉力橡胶胎套装于香槟金 6 辐条轮毂上，轮内集成随转向节联动的打孔通风刹车盘与赤红多活塞卡钳细节；由前 CVD 万向节驱动，支持 ±28° 转向与陀螺仪高频修正。",
    move: [-68, 48, 10],
  },
  wheels_r: {
    num: "10",
    name: "后 58mm 拉力轮总成 & 1.5° 内束角轮座",
    en: "Rear 58mm Rally Wheels & 1.5° Toe-in Hubs",
    spec: "Ø58 × 24 mm · 1.5° 固定内束角 (Toe-in) · 打孔刹车盘 + 快拆漂移胎环",
    colorTag: "香槟金 6 辐轮毂 + 赤红刹车卡钳",
    principle:
      "后轮座预设 1.5° 内束角（Toe-in）提供高速直线循迹性与出弯推力；同样配备 6 辐金色轮毂与内部打孔刹车盘/卡钳，可快速换装 POM 硬质漂移胎套实现四轮动力横滑。",
    move: [68, 48, 10],
  },
  upper_deck: {
    num: "11",
    name: "CNC 强化二楼板 & 前后防倾杆总成",
    en: "CNC Upper Chassis Brace & Front/Rear Sway Bars",
    spec: "贯通式铝合金二楼板加强梁 · 前后弹簧钢横向防倾杆 (Anti-Roll Bars)",
    colorTag: "阳极紫金加强梁 + 铬钢防倾杆",
    principle:
      "【新增结构总成】纵向桥接前后差速器波箱顶部的 CNC 铝合金二楼板（Upper Deck），与底板构成高刚度箱式抗扭笼；前后波箱同时引出弹簧钢横向防倾杆（Sway Bars）连至左右摆臂，在高速钟摆漂移时借扭转弹力抑制车身侧倾。",
    move: [0, 0, 56],
  },
  body_shell: {
    num: "12",
    name: "拉力空气动力学宽体车壳 & 双层高下压力尾翼",
    en: "Rally Aero Widebody Polycarbonate Shell & Wing",
    spec: "1.2 mm 聚碳酸酯宽体拉力壳 · 车顶冲压进气道 · 双层端板拉力尾翼 + R 扣",
    colorTag: "拉力赛车涂装 (支持透视/实心/隐藏)",
    principle:
      "【新增整车外观总成】复刻 WRC 传奇宽体掀背拉力赛车造型：前引擎盖散热百叶、车顶冲压进气风道（Roof Scoop）将冷空气直接导向 2845 无刷电机风扇，尾部双层大迎角拉力尾翼提供高速下压力。支持一键切换「X-Ray 半透明透视 / 实心涂装 / 隐藏车壳」。",
    move: [0, 0, 96],
  },
};

// Top-to-bottom mechanical disassembly sequence (outer shell & upper brace lift off first)
const ORDER = [
  "body_shell",
  "upper_deck",
  "suspension_f",
  "suspension_r",
  "motor",
  "esc",
  "battery",
  "servo",
  "drivetrain",
  "wheels_f",
  "wheels_r",
  "chassis",
];

// Build bench plate (stationary reference surface with 4 spinning dyno rollers & millimeter scale)
function buildBench() {
  const out = [`<path class="iso-halo" d="${k.haloOf(BENCH, BENCH_Z - FOOT_H, BENCH_H, P)}"/>`];
  for (const [x, y] of k.corners(BENCH, 22).sort((a, b) => depth(...a) - depth(...b))) {
    out.push(S(k.cylinder(x, y, 7.5, BENCH_Z - FOOT_H, 1.8, P, 24), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 5.6, BENCH_Z - FOOT_H + 1.8, FOOT_H - 1.8, P, 24), { tone: "mid" }));
  }
  out.push(S(k.slabOf(BENCH, BENCH_Z, BENCH_H, P, 8, 1.5), { tone: "lo" }));
  out.push(L(k.planOutline(k.insetPlan(BENCH, 6), BENCH_Z + BENCH_H, P), { tone: "faint" }));
  const zTop = BENCH_Z + BENCH_H;

  // 4 Under-Wheel Dyno Roller Beds (Twin Rollers under each wheel for live speed visualization)
  for (const ax of [AXLE_F, AXLE_R]) {
    for (const side of [-1, 1]) {
      const wy = side * TRACK_Y;
      const bed = { x: ax - 18, y: wy - 13, w: 36, d: 26, r: 3 };
      out.push(S(k.slabOf(bed, zTop - 0.5, 2.2, P, 4, 0.4), { tone: "mid" }));
      const F_R1 = G.frameOf([ax - 8, wy, zTop + 1.8], [0, 1, 0], [1, 0, 0], [0, 0, 1]);
      const F_R2 = G.frameOf([ax + 8, wy, zTop + 1.8], [0, 1, 0], [1, 0, 0], [0, 0, 1]);
      out.push(S(G.disc(-10, 10, 3.6, F_R1, P, { bevel: 0.4 }), { tone: "hi" }));
      out.push(S(G.disc(-10, 10, 3.6, F_R2, P, { bevel: 0.4 }), { tone: "hi" }));
    }
  }

  // Animated ground flow speed lines on the dyno deck
  for (const gy of [-78, -42, 0, 42, 78]) {
    out.push(
      L(k.segment([-148, gy, zTop + 0.3], [148, gy, zTop + 0.3], P), {
        tone: "faint",
        dashed: true,
        flow: true,
        className: "mjx-dyno-flow",
        free: true,
      }),
    );
  }

  // Center chassis standoffs supporting the 14303 chassis on the test rig
  for (const [sx, sy] of [[-48, -18], [-48, 18], [48, -18], [48, 18]]) {
    out.push(S(k.cylinder(sx, sy, 4.2, zTop, CHASSIS_Z - zTop, P, 20), { tone: "lo" }));
  }

  // Wheelbase ruler strip along front edge of bench
  const strip = { x: -124, y: BENCH.y + BENCH.d - 16, w: 248, d: 8, r: 1.2 };
  out.push(S(k.slabOf(strip, zTop, 0.7, P, 3), { tone: "mid", crease: "none" }));
  const ticks = k.topTicks(AXLE_F, AXLE_R, 6, 4, strip.y + 1, zTop + 0.7, [2.2, 4.2], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(
    k.faceTextSvg(
      k.topMatrix([0, strip.y + 5.8], zTop + 0.7, P, "x"),
      "MJX 14303 DYNO RIG · WB 192 MM · TRACK 125 MM · 4WD",
      { size: 2.7, tone: "mid", anchor: "middle" },
    ),
  );
  return out.join("");
}

// 01: 6061-T6 Aluminum Chassis Plate + Front EVA Bumper + LED Light Pods + Rear 5-Fin Diffuser
function buildChassis() {
  const out = [];
  out.push(`<path class="iso-halo" d="${k.haloOf(CHASSIS, CHASSIS_Z, CHASSIS_H, P)}" style="filter:blur(5px)"/>`);
  out.push(
    S(k.slabOf(CHASSIS, CHASSIS_Z, CHASSIS_H, P, 8, 0.9), {
      tone: "mid",
      inner: L(k.sideSeam(CHASSIS, CHASSIS_Z + 2.5, P, 8), { tone: "faint" }),
    }),
  );
  const zTop = CHASSIS_Z + CHASSIS_H;
  out.push(L(k.planOutline(k.insetPlan(CHASSIS, 4.5), zTop, P, 6), { tone: "lo" }));

  // CNC Honeycomb lightening pockets milled into chassis plate
  for (const hx of [-88, -28, 32, 72]) {
    const pocket = { x: hx, y: -9, w: 16, d: 18, r: 2 };
    out.push(L(k.planOutline(pocket, zTop, P, 4), { tone: "lo" }));
  }

  // Side mudguards / rock sliders with nerve ribs
  for (const side of [-1, 1]) {
    const guard = { x: -56, y: side > 0 ? 34 : -48, w: 112, d: 14, r: 3 };
    out.push(S(k.slabOf(guard, CHASSIS_Z + 1, 3.2, P, 4, 0.5), { tone: "lo" }));
    out.push(L(k.planOutline(k.insetPlan(guard, 2), CHASSIS_Z + 4.2, P, 3), { tone: "faint" }));
    out.push(D([[-44, guard.y + 7, CHASSIS_Z + 4.2], [-15, guard.y + 7, CHASSIS_Z + 4.2], [15, guard.y + 7, CHASSIS_Z + 4.2], [44, guard.y + 7, CHASSIS_Z + 4.2]].map(at), { size: 0.45 }));
  }

  // Front wide EVA foam rally bumper + front lower lip splitter (-144 to -114)
  const splitter = { x: -146, y: -55, w: 18, d: 110, r: 6 };
  out.push(S(k.slabOf(splitter, CHASSIS_Z - 2.2, 2.2, P, 5, 0.4), { tone: "hi" }));
  const bumper = { x: -142, y: -52, w: 24, d: 104, r: 9 };
  out.push(S(k.slabOf(bumper, CHASSIS_Z - 0.5, 7.5, P, 6, 1.0), { tone: "lo" }));
  out.push(L(k.planOutline(k.insetPlan(bumper, 3), CHASSIS_Z + 7, P, 4), { tone: "faint" }));

  // Front Dual Rally LED Fog-Light Pods + Angel-Eye Halos + Aero Canards mounted on bumper
  const braceF = { x: -132, y: -32, w: 14, d: 64, r: 3 };
  out.push(S(k.slabOf(braceF, CHASSIS_Z + 7, 3, P, 4, 0.4), { tone: "mid" }));
  const F_LED_L = G.frameOf([-136, -26, CHASSIS_Z + 8.5], [-1, 0, 0], [0, 1, 0], [0, 0, 1]);
  const F_LED_R = G.frameOf([-136, 26, CHASSIS_Z + 8.5], [-1, 0, 0], [0, 1, 0], [0, 0, 1]);
  out.push(`<g class="mjx-headlight-pod">${S(G.disc(-3, 2, 4.4, F_LED_L, P, { bevel: 0.4 }), { tone: "hi", lit: true })}${S(G.disc(-3, 2, 4.4, F_LED_R, P, { bevel: 0.4 }), { tone: "hi", lit: true })}</g>`);
  // Side aerodynamic dive-plane canards on front bumper corners
  for (const side of [-1, 1]) {
    const canard = { x: -140, y: side > 0 ? 49 : -53, w: 16, d: 4, r: 1 };
    out.push(S(k.slabOf(canard, CHASSIS_Z + 2, 4.8, P, 3, 0.3), { tone: "hi" }));
  }

  // Front & Rear Body Mounting Posts with height adjustment pin holes
  for (const [px, py] of [[-125, -22], [-125, 22], [112, -22], [112, 22]]) {
    out.push(S(k.cylinder(px, py, 2.4, CHASSIS_Z + 9, 22, P, 16), { tone: "mid" }));
    out.push(S(k.cylinder(px, py, 3.5, CHASSIS_Z + 31, 2.2, P, 16), { tone: "hi" }));
  }

  // Rear 5-fin aerodynamic diffuser bumper (+114 to +136)
  const bumperR = { x: 116, y: -44, w: 20, d: 88, r: 5 };
  out.push(S(k.slabOf(bumperR, CHASSIS_Z, 6, P, 5, 0.7), { tone: "lo" }));
  for (const dy of [-28, -14, 0, 14, 28]) {
    out.push(S(k.slabOf({ x: 120, y: dy - 1.2, w: 16, d: 2.4, r: 0.5 }, CHASSIS_Z - 1, 7.8, P, 2), { tone: "hi" }));
  }

  // Countersunk chassis screws
  out.push(D(k.dotGrid(-36, -12, 4, 2, 16, zTop, P), { size: 0.42, tone: "lo" }));
  return out.join("");
}

// 02: LIT SUBJECT — Full-Time 4WD Metal Drivetrain (Center Shaft, Spur/Pinion, Planetary Bevel Diffs, CVD Dogbones)
function buildDrivetrain() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;
  const shaftZ = zTop + 9;
  const F_X = G.frameOf([0, 0, shaftZ], [1, 0, 0], [0, 1, 0], [0, 0, 1]);

  // Front & Rear Cutaway Differential Housings + Internal 37T Bevel Ring Gear + 4 Planetary Satellites
  for (const ax of [AXLE_F, AXLE_R]) {
    const housing = { x: ax - 13, y: -15, w: 26, d: 30, r: 4 };
    out.push(S(k.slabOf(housing, zTop, 16, P, 5, 0.8), { tone: "mid" }));
    out.push(L(k.planOutline(k.insetPlan(housing, 2.5), zTop + 16, P, 4), { tone: "lo" }));
    out.push(D(k.corners(housing, 3.5).map(([x, y]) => at([x, y, zTop + 16])), { size: 0.45 }));

    // Lit 37T Metal Bevel Ring Gear + 4 Planetary Satellite Gears inside diff cup
    const F_Y = G.frameOf([ax, 0, shaftZ], [0, 1, 0], [1, 0, 0], [0, 0, 1]);
    out.push(S(G.disc(-5.5, 5.5, 8.2, F_Y, P, { bevel: 0.5 }), { tone: "hi", lit: true }));
    out.push(S(G.disc(-2.2, 2.2, 10.6, F_Y, P, { bevel: 0.6 }), { tone: "hi", lit: true }));
    out.push(D(G.dotsOf(F_Y, 2.4, 6.2, 8, P, { all: true }), { size: 0.52, tone: "lo" }));

    // 13T Input Attack Pinion Gear where Center Shaft enters Diff Housing
    const pinOffset = ax < 0 ? 14 : -14;
    const F_ATTACK = G.frameOf([ax + pinOffset, 0, shaftZ], [1, 0, 0], [0, 1, 0], [0, 0, 1]);
    out.push(S(G.disc(-3, 3, 4.8, F_ATTACK, P, { bevel: 0.4 }), { tone: "hi", lit: true }));

    // Left & Right Metal CVD Driveshafts (Dogbones) out to Wheel Hubs
    for (const side of [-1, 1]) {
      const y0 = side * 15;
      const y1 = side * (TRACK_Y - 8);
      const route = [
        [ax, y0, shaftZ],
        [ax, y1, WHEEL_Z],
      ];
      for (const part of tubePieces(route, 2.1, P, { maxLength: 60 })) {
        out.push(tubeSvg(part, { tone: "hi" }));
      }
      out.push(S(G.disc(side > 0 ? 13 : -17, side > 0 ? 17 : -13, 3.8, F_Y, P), { tone: "hi", lit: true }));
    }
  }

  // Center Aluminum Main Driveshaft running from AXLE_F + 14 to AXLE_R - 14 with phase collars
  out.push(S(G.disc(AXLE_F + 14, AXLE_R - 14, 3.1, F_X, P, { bevel: 0.4 }), { tone: "hi", lit: true }));
  for (const sx of [-48, -16, 12, 54]) {
    out.push(S(G.disc(sx - 1.2, sx + 1.2, 4.1, F_X, P, { bevel: 0.3 }), { tone: "mid", lit: true }));
  }

  // 45T Metal Spur Gear + Slipper Clutch Hub at x = 38
  out.push(S(G.disc(34, 40, 13.5, F_X, P, { bevel: 0.7 }), { tone: "hi", lit: true }));
  out.push(S(G.disc(31.5, 42.5, 6.4, F_X, P, { bevel: 0.4 }), { tone: "hi", lit: true }));
  out.push(D(G.dotsOf(F_X, 40.2, 9.8, 12, P, { all: true }), { size: 0.48, tone: "lo" }));

  // 15T Steel Pinion Gear meshing with 45T Spur Gear (offset at y = +15.5, z = shaftZ + 2)
  const F_PINION = G.frameOf([37, 15.5, shaftZ + 2], [1, 0, 0], [0, 1, 0], [0, 0, 1]);
  out.push(S(G.disc(-4.2, 4.2, 5.5, F_PINION, P, { bevel: 0.4 }), { tone: "hi", lit: true }));

  // Animated flow lines along center drivetrain & front/rear axles for visual torque flow
  out.push(
    L(k.segment([AXLE_F, 0, shaftZ + 10], [AXLE_R, 0, shaftZ + 10], P), {
      tone: "lit",
      dashed: true,
      flow: true,
      className: "mjx-torque-line",
      free: true,
    }),
  );
  return out.join("");
}

// 03: 2845 3700KV 4-Pole Brushless Motor + 6-Ring Anodized Heatsink + 6-Blade Turbine Cooling Fan
function buildMotor() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;
  const motorZ = zTop + 11;
  const F_M = G.frameOf([8, 15.5, motorZ], [1, 0, 0], [0, 1, 0], [0, 0, 1]);

  // CNC Motor Mount Bulkhead
  out.push(S(k.slabOf({ x: 25, y: 4, w: 6, d: 24, r: 1.5 }, zTop, 20, P, 3, 0.5), { tone: "mid" }));

  // 2845 Brushless Can (x = -16 to +25, radius = 10.5)
  out.push(S(G.disc(-16, 25, 10.5, F_M, P, { bevel: 0.8 }), { tone: "hi" }));

  // 6-Ring Anodized Finned Heatsink Jacket around motor body
  for (const s of [-12, -6.5, -1, 4.5, 10, 15.5]) {
    out.push(S(G.disc(s - 1.1, s + 1.1, 12.4, F_M, P, { bevel: 0.35 }), { tone: "mid" }));
  }

  // Top 30x30 High-RPM Cooling Fan with 6 turbine blade spokes
  const fanPlan = { x: -10, y: 4.5, w: 22, d: 22, r: 2.5 };
  const fanZ = motorZ + 12.5;
  out.push(S(k.slabOf(fanPlan, fanZ, 5.5, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.ring(1, 15.5, 8.8, fanZ + 5.5, P, 28), { tone: "lo" }));
  const fanBlades = Array.from({ length: 6 }, (_, i) => {
    const a = (i * Math.PI) / 3;
    return k.segment(
      [1 + Math.cos(a) * 3.2, 15.5 + Math.sin(a) * 3.2, fanZ + 5.5],
      [1 + Math.cos(a + 0.35) * 8.4, 15.5 + Math.sin(a + 0.35) * 8.4, fanZ + 5.5],
      P,
    );
  }).join("");
  out.push(`<g class="mjx-fan-blades">${L(fanBlades, { tone: "hi", free: true })}</g>`);
  out.push(S(k.cylinder(1, 15.5, 3.3, fanZ + 4, 1.9, P, 18), { tone: "hi" }));
  out.push(D(k.corners(fanPlan, 2.6).map(([x, y]) => at([x, y, fanZ + 5.5])), { size: 0.45 }));

  // 3-Phase Brushless Silicone Wires (U/V/W) from Motor to 45A ESC
  for (const [idx, dy] of [-3, 0, 3].entries()) {
    const route = [
      [-16, 15.5 + dy, motorZ + 3],
      [-24, 10 + dy * 1.4, motorZ + 10],
      [-24, -6 + dy * 1.4, motorZ + 10],
    ];
    for (const part of tubePieces(route, 1.3, P, { maxLength: 30 })) {
      out.push(tubeSvg(part, { tone: idx === 1 ? "hi" : "mid" }));
    }
  }
  return out.join("");
}

// 04: E45R 45A Brushless ESC + Super-Capacitors + G3C Gyro Receiver Box
function buildEsc() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;

  // 45A ESC base + 7-fin anodized heatsink + dual capacitor bank
  const escPlan = { x: -42, y: -32, w: 28, d: 24, r: 2.5 };
  out.push(S(k.slabOf(escPlan, zTop, 11, P, 4, 0.6), { tone: "mid" }));
  for (let fx = escPlan.x + 2.5; fx < escPlan.x + escPlan.w - 2.5; fx += 3.6) {
    out.push(S(k.slabOf({ x: fx, y: escPlan.y + 3, w: 1.9, d: 18, r: 0.4 }, zTop + 11, 5.2, P, 2), { tone: "hi" }));
  }
  // Dual super-capacitor cylinders + power switch beside ESC
  out.push(S(k.cylinder(-11, -26, 3.2, zTop, 11.5, P, 18), { tone: "hi" }));
  out.push(S(k.cylinder(-11, -18, 3.2, zTop, 11.5, P, 18), { tone: "hi" }));

  // G3C Gyro 3-Channel Receiver Box behind ESC + Gyro Status Indicator LED
  const rxPlan = { x: -64, y: -32, w: 18, d: 22, r: 2 };
  out.push(S(k.slabOf(rxPlan, zTop, 12, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(rxPlan, 2), zTop + 12, P, 3), { tone: "lo" }));
  out.push(S(k.cylinder(-50, -15, 1.6, zTop + 12, 1.4, P, 14), { tone: "hi", lit: true }));
  out.push(
    k.faceTextSvg(k.topMatrix([-55, -21], zTop + 12, P, "x"), "G3C GYRO", {
      size: 2.3,
      tone: "hi",
      anchor: "middle",
    }),
  );
  // 2.4GHz Vertical Antenna Tube
  out.push(S(k.cylinder(-60, -28, 1.1, zTop + 12, 28, P, 12), { tone: "hi" }));
  out.push(S(k.cylinder(-60, -28, 1.6, zTop + 40, 2.5, P, 12), { tone: "lo" }));
  return out.join("");
}

// 05: 7.4V 2S / 11.1V 3S LiPo Battery Pack + Hold-Down Strap + XT60 Connector & Balance Lead
function buildBattery() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;
  const tray = { x: -2, y: -34, w: 66, d: 26, r: 3 };
  out.push(S(k.slabOf(tray, zTop, 2.5, P, 4, 0.4), { tone: "lo" }));

  const pack = { x: 1, y: -32, w: 60, d: 22, r: 3 };
  out.push(
    S(k.slabOf(pack, zTop + 2.5, 16, P, 5, 0.9), {
      tone: "mid",
      inner: L(k.sideSeam(pack, zTop + 10.5, P, 5), { tone: "lo" }),
    }),
  );
  out.push(L(k.planOutline(k.insetPlan(pack, 2.5), zTop + 18.5, P, 4), { tone: "faint" }));
  out.push(
    k.faceTextSvg(k.topMatrix([31, -21], zTop + 18.5, P, "x"), "2S/3S HIGH-C LIPO", {
      size: 2.6,
      tone: "hi",
      anchor: "middle",
    }),
  );

  // Upper hold-down strap bar & posts
  out.push(S(k.cylinder(31, -34, 2.0, zTop, 20.5, P, 14), { tone: "mid" }));
  out.push(S(k.cylinder(31, -8, 2.0, zTop, 20.5, P, 14), { tone: "mid" }));
  out.push(S(k.slabOf({ x: 26, y: -35, w: 10, d: 28, r: 1.5 }, zTop + 18.8, 2.2, P, 3, 0.4), { tone: "hi" }));

  // Amber XT60 High-Current Plug & JST Balance Plug on front end of battery pack
  const xt60 = { x: -7, y: -27, w: 7, d: 10, r: 1.2 };
  out.push(S(k.slabOf(xt60, zTop + 9, 6, P, 3, 0.4), { tone: "hi", lit: true }));
  const jst = { x: -5, y: -15, w: 5, d: 6, r: 0.8 };
  out.push(S(k.slabOf(jst, zTop + 10, 4, P, 2, 0.3), { tone: "hi" }));
  return out.join("");
}

// 06: 17g Digital Steering Servo + Spring Servo Saver + Dual-Bellcrank Ackermann Rack
function buildServo() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;

  // 17g Digital Servo Body (front-right of chassis) with mounting ears
  const servoPlan = { x: -56, y: 10, w: 26, d: 14, r: 2 };
  out.push(S(k.slabOf(servoPlan, zTop, 16, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.sideSeam(servoPlan, zTop + 11, P, 4), { tone: "lo" }));
  out.push(S(k.cylinder(-50, 17, 4.4, zTop + 16, 2.5, P, 20), { tone: "hi" }));
  out.push(D([at([-50, 17, zTop + 18.5])], { size: 0.5, tone: "lo" }));

  // Dual-Bellcrank Steering Posts + Spring Servo Saver Column + Ackermann Tie-Rod Plate
  for (const py of [-11, 11]) {
    out.push(S(k.cylinder(-68, py, 3.8, zTop, 14, P, 20), { tone: "mid" }));
    out.push(S(k.cylinder(-68, py, 2.4, zTop + 14, 3, P, 16), { tone: "hi" }));
  }
  const dragLink = { x: -71, y: -13, w: 6, d: 26, r: 2 };
  out.push(S(k.slabOf(dragLink, zTop + 11, 2.8, P, 3, 0.4), { tone: "hi" }));

  // Adjustable turnbuckle tie rods out to front steering knuckles
  for (const side of [-1, 1]) {
    const route = [
      [-68, side * 11, zTop + 12],
      [AXLE_F + 5, side * (TRACK_Y - 12), WHEEL_Z - 2],
    ];
    for (const part of tubePieces(route, 1.35, P, { maxLength: 50 })) {
      out.push(tubeSvg(part, { tone: "hi" }));
    }
  }
  return out.join("");
}

// 07 & 08: Front & Rear Independent Double-Wishbone Suspension + CNC Shock Tower + Oil-Filled Coilovers
function buildSuspension(isFront) {
  const out = [];
  const ax = isFront ? AXLE_F : AXLE_R;
  const zTop = CHASSIS_Z + CHASSIS_H;

  // CNC Aluminum Shock Tower (Butterfly mount) with multiple shock-angle tuning holes
  const towerX = isFront ? ax + 6 : ax - 10;
  const tower = { x: towerX, y: -24, w: 4.5, d: 48, r: 1.5 };
  out.push(S(k.slabOf(tower, zTop + 14, 22, P, 4, 0.5), { tone: "hi" }));
  out.push(
    D(
      [
        [-20, zTop + 33],
        [-16, zTop + 33],
        [-12, zTop + 33],
        [12, zTop + 33],
        [16, zTop + 33],
        [20, zTop + 33],
      ].map(([y, z]) => at([towerX + 2.2, y, z])),
      { size: 0.45 },
    ),
  );

  // Left & Right Lower A-Arms, Upper Camber Links, and Oil-Filled Coilover Shocks
  for (const side of [-1, 1]) {
    const yInner = side * 14;
    const yOuter = side * (TRACK_Y - 10);
    const armPlan = {
      x: ax - 9.5,
      y: side > 0 ? yInner : yOuter,
      w: 19,
      d: Math.abs(yOuter - yInner),
      r: 2.5,
    };
    out.push(S(k.slabOf(armPlan, zTop + 1, 3.4, P, 4, 0.4), { tone: "mid" }));
    out.push(L(k.planOutline(k.insetPlan(armPlan, 2.4), zTop + 4.4, P, 3), { tone: "lo" }));

    const upperRoute = [
      [ax, side * 13, zTop + 15],
      [ax, side * (TRACK_Y - 11), WHEEL_Z + 7],
    ];
    for (const part of tubePieces(upperRoute, 1.45, P, { maxLength: 45 })) {
      out.push(tubeSvg(part, { tone: "hi" }));
    }

    const shockX = towerX + 2.2;
    const shockY = side * 22;
    const zBot = zTop + 5;
    const zSpringTop = zTop + 25;
    const zCapTop = zTop + 33.5;

    const springRings = Array.from({ length: 7 }, (_, i) =>
      k.ring(shockX, shockY, 3.9, zBot + 2 + ((zSpringTop - zBot - 4) * (i + 0.5)) / 7, P, 18),
    ).join("");
    out.push(S(k.cylinder(shockX, shockY, 1.7, zBot, zSpringTop - zBot, P, 14), { tone: "hi", crease: "none" }));
    out.push(L(springRings, { tone: "hi" }));
    out.push(S(k.cylinder(shockX, shockY, 3.8, zSpringTop - 7, zCapTop - (zSpringTop - 7), P, 20, 0.5), { tone: "hi" }));
    out.push(L(k.knurl(shockX, shockY, 4.0, zSpringTop - 2.2, zSpringTop, 18, P), { tone: "lo" }));
  }
  return out.join("");
}

// 09 & 10: Front & Rear 58mm Rally/Drift Wheels, 6-Spoke Rims, Cross-Drilled Brake Discs & Red Calipers
function buildWheels(isFront) {
  const out = [];
  const ax = isFront ? AXLE_F : AXLE_R;
  const sides = [-1, 1].sort((a, b) => depth(ax, a * TRACK_Y, WHEEL_Z) - depth(ax, b * TRACK_Y, WHEEL_Z));

  for (const side of sides) {
    const wy = side * TRACK_Y;
    const F_W = G.frameOf([ax, wy, WHEEL_Z], [0, side, 0], [1, 0, 0], [0, 0, 1]);
    const partAttr = isFront ? `data-wheel="front-${side > 0 ? "r" : "l"}"` : `data-wheel="rear-${side > 0 ? "r" : "l"}"`;

    const wheelGroup = [];
    // Inner Cross-Drilled Brake Rotor + Brake Caliper inside steering knuckle
    wheelGroup.push(S(G.disc(-WHEEL_W / 2 - 4.5, -WHEEL_W / 2 - 1.2, 11.5, F_W, P, { bevel: 0.4 }), { tone: "mid" }));
    wheelGroup.push(D(G.dotsOf(F_W, -WHEEL_W / 2 - 1.1, 8.2, 10, P, { all: true }), { size: 0.45, tone: "lo" }));
    // Brake caliper block on rotor
    const calX = isFront ? ax + 5 : ax - 9;
    const calY = wy - side * (WHEEL_W / 2 + 4);
    wheelGroup.push(S(k.slabOf({ x: calX, y: calY - 2, w: 6, d: 4, r: 1 }, WHEEL_Z + 5, 7, P, 3, 0.3), { tone: "hi", lit: true }));

    // Rubber Rally Tire Carcass with tread grooves
    wheelGroup.push(
      S(G.disc(-WHEEL_W / 2, WHEEL_W / 2, WHEEL_R, F_W, P, { bevel: 1.5 }), {
        tone: "lo",
        inner: L(
          [-5, -1.6, 1.6, 5].map((s) => G.arcOf(F_W, s, WHEEL_R, P)).join(""),
          { tone: "faint" },
        ),
      }),
    );

    // 6-Spoke Rally Rim Face + Outer Beadlock Ring
    wheelGroup.push(S(G.disc(WHEEL_W / 2 - 2.4, WHEEL_W / 2 + 0.5, WHEEL_R * 0.68, F_W, P, { bevel: 0.6 }), { tone: "hi" }));
    wheelGroup.push(D(G.dotsOf(F_W, WHEEL_W / 2 + 0.6, WHEEL_R * 0.56, 12, P, { all: true }), { size: 0.42, tone: "lo" }));

    // 6 Sculpted Rim Spokes (connected to wheel spin animation)
    const rimY = wy + side * (WHEEL_W / 2 + 0.6);
    const spokesD = Array.from({ length: 6 }, (_, i) => {
      const a = (i * Math.PI) / 3;
      const p0 = [ax + Math.cos(a) * 4.2, rimY, WHEEL_Z + Math.sin(a) * 4.2];
      const p1 = [ax + Math.cos(a) * (WHEEL_R * 0.62), rimY, WHEEL_Z + Math.sin(a) * (WHEEL_R * 0.62)];
      return k.segment(p0, p1, P);
    }).join("");
    wheelGroup.push(`<g class="mjx-wheel-spokes">${L(spokesD, { tone: "lo", free: true })}</g>`);

    // 12mm Hex Center Wheel Locknut
    wheelGroup.push(S(G.disc(WHEEL_W / 2 + 0.5, WHEEL_W / 2 + 2.4, 4.0, F_W, P), { tone: "mid", lit: true }));
    wheelGroup.push(D(G.dotsOf(F_W, WHEEL_W / 2 + 0.6, WHEEL_R * 0.38, 6, P, { all: true }), { size: 0.55, tone: "lo" }));

    out.push(`<g ${partAttr}>${wheelGroup.join("")}</g>`);
  }
  return out.join("");
}

// 11: NEW — CNC Aluminum Upper Chassis Stiffener Deck & Front/Rear Anti-Roll Sway Bars
function buildUpperDeck() {
  const out = [];
  const zDeck = 23.5;

  // Longitudinal CNC Aluminum Upper Stiffener Brace bridging front & rear diff bulkheads
  const brace = { x: AXLE_F + 10, y: -5.5, w: AXLE_R - AXLE_F - 20, d: 11, r: 2.5 };
  out.push(S(k.slabOf(brace, zDeck, 2.6, P, 5, 0.5), { tone: "hi" }));
  out.push(L(k.planOutline(k.insetPlan(brace, 2), zDeck + 2.6, P, 3), { tone: "lo" }));

  // Triangular lightening cutouts & mounting bolts along the upper deck
  for (const cx of [-52, -26, 0, 26, 52]) {
    out.push(D([[cx, -2.5, zDeck + 2.6], [cx, 2.5, zDeck + 2.6]].map(at), { size: 0.48, tone: "lo" }));
  }
  out.push(
    k.faceTextSvg(k.topMatrix([0, 0.8], zDeck + 2.6, P, "x"), "HYPER GO · CNC UPPER BRACE", {
      size: 2.3,
      tone: "lo",
      anchor: "middle",
    }),
  );

  // Front & Rear Spring-Steel Anti-Roll Sway Bars
  for (const ax of [AXLE_F, AXLE_R]) {
    const swayX = ax < 0 ? ax + 15 : ax - 15;
    const swayRoute = [
      [swayX, -24, zDeck - 1],
      [swayX, -14, zDeck + 1],
      [swayX, 14, zDeck + 1],
      [swayX, 24, zDeck - 1],
    ];
    for (const part of tubePieces(swayRoute, 1.15, P, { maxLength: 40 })) {
      out.push(tubeSvg(part, { tone: "hi" }));
    }
  }
  return out.join("");
}

// 12: NEW — 1/14 Rally Aero Widebody Polycarbonate Body Shell, Roof Scoop & Dual-Plane Rear Wing
function buildBodyShell() {
  const out = [];
  const zBase = 39;

  // Lower beltline rally widebody skirt & hood/fender silhouette
  const lowerBody = { x: -112, y: -44, w: 224, d: 88, r: 12 };
  out.push(
    S(k.slabOf(lowerBody, zBase, 8.5, P, 8, 1.2), {
      tone: "mid",
      inner: L(k.sideSeam(lowerBody, zBase + 4.2, P, 8), { tone: "lo" }),
    }),
  );
  out.push(L(k.planOutline(k.insetPlan(lowerBody, 4), zBase + 8.5, P, 6), { tone: "lo" }));

  // Hood vents & rally livery stripes on front hood (-102 to -42)
  for (const vy of [-18, 10]) {
    const vent = { x: -94, y: vy, w: 32, d: 8, r: 1.5 };
    out.push(L(k.planOutline(vent, zBase + 8.5, P, 3), { tone: "hi" }));
  }
  out.push(
    k.faceTextSvg(k.topMatrix([-76, 0], zBase + 8.6, P, "x"), "MJX HYPER GO · 14303 RALLY", {
      size: 2.8,
      tone: "hi",
      anchor: "middle",
    }),
  );

  // Aerodynamic Cabin Greenhouse & Windshield/Windows (-42 to +68)
  const cabin = { x: -42, y: -35, w: 108, d: 70, r: 10 };
  out.push(
    S(k.slabOf(cabin, zBase + 8.5, 13, P, 7, 1.8), {
      tone: "hi",
      inner: L(k.sideSeam(cabin, zBase + 15, P, 7), { tone: "lo" }),
    }),
  );
  out.push(L(k.planOutline(k.insetPlan(cabin, 5), zBase + 21.5, P, 5), { tone: "lo" }));

  // Rally Roof Ram-Air Scoop feeding cool air toward the 2845 motor fan + Roof Shark-Fin Vortex Generators
  const scoop = { x: -16, y: -11, w: 38, d: 22, r: 3 };
  out.push(S(k.slabOf(scoop, zBase + 21.5, 4.2, P, 4, 0.7), { tone: "hi", lit: true }));
  for (const vy of [-20, -10, 0, 10, 20]) {
    out.push(S(k.slabOf({ x: 48, y: vy - 0.7, w: 7, d: 1.4, r: 0.3 }, zBase + 21.5, 2.2, P, 2), { tone: "hi" }));
  }

  // Left & Right Rally Aero Wing Mirrors + Front/Rear Integrated LED Light Bars on Body Shell
  for (const side of [-1, 1]) {
    const mirror = { x: -34, y: side > 0 ? 35 : -41, w: 9, d: 6, r: 1.8 };
    out.push(S(k.slabOf(mirror, zBase + 10.5, 3.6, P, 3, 0.4), { tone: "hi", lit: true }));
  }
  const frontLightBar = { x: -113, y: -28, w: 4, d: 56, r: 1.2 };
  const rearTailBar = { x: 109, y: -30, w: 4, d: 60, r: 1.2 };
  out.push(`<g class="mjx-headlight-pod">${S(k.slabOf(frontLightBar, zBase + 3.2, 2.8, P, 3, 0.3), { tone: "hi", lit: true })}${S(k.slabOf(rearTailBar, zBase + 4.2, 2.6, P, 3, 0.3), { tone: "hi", lit: true })}</g>`);

  // High-Downforce Dual-Plane Rally Rear Wing (+78 to +110)
  for (const wy of [-24, 24]) {
    // Wing struts
    out.push(S(k.slabOf({ x: 80, y: wy - 1.5, w: 14, d: 3, r: 0.8 }, zBase + 8.5, 14, P, 3, 0.3), { tone: "mid" }));
  }
  // Lower & Upper Rear Wing Elements + Side Endplates
  const wingLower = { x: 82, y: -40, w: 20, d: 80, r: 3 };
  const wingUpper = { x: 86, y: -42, w: 22, d: 84, r: 3.5 };
  out.push(S(k.slabOf(wingLower, zBase + 16, 2.2, P, 4, 0.4), { tone: "mid" }));
  out.push(S(k.slabOf(wingUpper, zBase + 22, 2.6, P, 4, 0.5), { tone: "hi", lit: true }));
  for (const side of [-1, 1]) {
    const endplate = { x: 80, y: side > 0 ? 40 : -43.5, w: 28, d: 3.5, r: 1 };
    out.push(S(k.slabOf(endplate, zBase + 13, 13.5, P, 3, 0.4), { tone: "hi" }));
  }

  // 4 R-Type Metal Body Clips on hood & trunk
  for (const [bx, by] of [[-96, -22], [-96, 22], [72, -22], [72, 22]]) {
    out.push(S(k.cylinder(bx, by, 2.8, zBase + 8.5, 1.4, P, 14), { tone: "hi", lit: true }));
  }

  // Aero Streamlines flowing over hood, roof scoop, and rear wing
  for (const ay of [-24, 0, 24]) {
    out.push(
      L(
        k.pathOf(
          [
            at([-125, ay, zBase + 5]),
            at([-60, ay, zBase + 12]),
            at([10, ay, zBase + 28]),
            at([110, ay, zBase + 30]),
          ],
          false,
        ),
        { tone: "lit", dashed: true, flow: true, className: "mjx-aero-line", free: true },
      ),
    );
  }
  return out.join("");
}

// Compute back-to-front painter's order + Audit Recorder registration
const R = A.recorder(P, {
  order: ORDER,
  spring: { stagger: 0, stiffness: 78, damping: 15, substeps: 4 },
});

const RAW_PARTS = [
  { id: "chassis", anchor: true, ref: [0, 0, 4], box: [[-118, -38, 2], [118, 38, 7]], svg: buildChassis() },
  { id: "suspension_f", ref: [AXLE_F, -18, 22], box: [[-92, -32, 7], [-76, -12, 36]], svg: buildSuspension(true) },
  { id: "suspension_r", ref: [AXLE_R, -18, 22], box: [[76, -32, 7], [92, -12, 36]], svg: buildSuspension(false) },
  { id: "battery", ref: [28, -22, 14], box: [[4, -30, 7], [58, -12, 24]], svg: buildBattery() },
  { id: "esc", ref: [-48, -22, 14], box: [[-62, -30, 7], [-16, -12, 23]], svg: buildEsc() },
  { id: "drivetrain", ref: [0, 0, 14], box: [[-68, -4, 7], [68, 4, 20]], svg: buildDrivetrain() },
  { id: "servo", ref: [-50, 18, 14], box: [[-64, 12, 7], [-32, 24, 23]], svg: buildServo() },
  { id: "motor", ref: [8, 18, 18], box: [[-14, 8, 7], [26, 26, 28]], svg: buildMotor() },
  { id: "upper_deck", ref: [0, 0, 22], box: [[-66, -4, 20], [66, 4, 24]], svg: buildUpperDeck() },
  { id: "wheels_f", anchor: true, ref: [AXLE_F, 48, WHEEL_Z], box: [[-104, 52, 0], [-64, 70, 36]], svg: buildWheels(true) },
  { id: "wheels_r", anchor: true, ref: [AXLE_R, 48, WHEEL_Z], box: [[64, 52, 0], [104, 70, 36]], svg: buildWheels(false) },
  { id: "body_shell", ref: [0, 0, 50], box: [[-92, -32, 36], [92, 32, 62]], svg: buildBodyShell() },
];

for (const item of RAW_PARTS) {
  const shape = R.solid(A.box(item.box[0], item.box[1], { name: `${item.id}.hull`, ground: Boolean(item.anchor) }));
  R.put({
    piece: item.id,
    ride: item.id,
    at: item.ref,
    svg: item.svg,
    move: PIECES[item.id].move,
    shapes: [shape],
    name: `${item.id}.main`,
  });
}

A.settle(R, P, { step: 1.0 });
R.items.sort((a, b) => a.key - b.key);

const svgBody = [
  buildBench(),
  ...R.items.map((item) => {
    const m = PIECES[item.piece].move;
    return `<g class="mjx-piece" data-piece="${item.piece}" data-move="${m.join(",")}">${item.svg}</g>`;
  }),
];

const svg = k.figureSvg({
  width: WIDTH,
  height: HEIGHT,
  label:
    "美嘉欣 MJX Hyper Go 14303 (1/14 4WD 无刷拉力/漂移整车) 12 总成等轴测机械解剖图：包含 6061-T6 铝合金蜂窝底盘、中央金属主传动轴与前后行星齿轮差速器、2845 3700KV 四极无刷电机与涡轮风扇、45A 电调与 G3C 陀螺仪接收机、2S/3S 锂电池与 XT60、17g 数字舵机阿克曼转向、四轮油压绞牙悬架、6 辐轮毂与通风刹车盘、CNC 二楼板防倾杆及可透视拉力宽体车壳尾翼。",
  body: svgBody,
});

const CSS = `
.mjx-wrap{max-width:1020px;margin:0 auto}
.mjx-topbar{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:10px;padding:10px 16px;border-top:1px solid var(--anatomy-faint);background:color-mix(in srgb,var(--anatomy-paper) 88%,var(--anatomy-lit) 12%)}
.mjx-topbar-group{display:flex;flex-wrap:wrap;align-items:center;gap:6px;font-size:12px}
.mjx-topbar-label{font-weight:700;color:var(--anatomy-hi);margin-right:4px}
.mjx-toolbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;padding:12px 16px;border-top:1px solid var(--anatomy-faint);background:color-mix(in srgb,var(--anatomy-paper) 92%,var(--anatomy-lo) 8%)}
.mjx-ctrl{display:flex;flex-direction:column;gap:5px;font-size:12px;color:var(--anatomy-mid)}
.mjx-ctrl-head{display:flex;justify-content:space-between;align-items:center;font-weight:600;color:var(--anatomy-hi)}
.mjx-btn-row{display:flex;flex-wrap:wrap;gap:5px}
.mjx-btn{appearance:none;border:1px solid var(--anatomy-lo);background:var(--anatomy-paper);color:var(--anatomy-hi);padding:5px 9px;border-radius:4px;font-size:11.5px;font-family:inherit;cursor:pointer;transition:all .15s}
.mjx-btn:hover{border-color:var(--anatomy-hi)}
.mjx-btn[data-active]{background:var(--anatomy-lit);color:#111;border-color:var(--anatomy-lit);font-weight:700}
.mjx-slider{width:100%;accent-color:var(--anatomy-lit);cursor:pointer}
.mjx-telemetry{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;padding:10px 16px;border-top:1px solid var(--anatomy-faint);font-variant-numeric:tabular-nums}
.mjx-stat{padding:6px 10px;border:1px solid var(--anatomy-faint);border-radius:4px;background:color-mix(in srgb,var(--anatomy-paper) 96%,var(--anatomy-hi) 4%)}
.mjx-stat-label{font-size:10.5px;color:var(--anatomy-mid);text-transform:uppercase;letter-spacing:.04em}
.mjx-stat-val{font-size:14.5px;font-weight:700;color:var(--anatomy-hi);margin-top:2px}
.mjx-stat-val[data-lit]{color:var(--anatomy-lit)}
.mjx-scope-bar{display:grid;grid-template-columns:1fr 260px;gap:12px;padding:10px 16px;border-top:1px solid var(--anatomy-faint);align-items:center;background:color-mix(in srgb,var(--anatomy-paper) 95%,var(--anatomy-lo) 5%)}
.mjx-scope-canvas{width:100%;height:76px;border:1px solid var(--anatomy-faint);border-radius:4px;background:color-mix(in srgb,var(--anatomy-paper) 90%,#000 10%)}
.mjx-scope-legend{font-size:11.5px;color:var(--anatomy-mid);display:flex;flex-direction:column;gap:4px}
.mjx-scope-item{display:flex;align-items:center;gap:6px}
.mjx-dot{width:9px;height:9px;border-radius:50%;display:inline-block}
.mjx-parts-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:6px;margin-bottom:12px}
.mjx-part-btn{appearance:none;text-align:left;border:1px solid var(--anatomy-faint);background:transparent;color:var(--anatomy-mid);padding:6px 9px;border-radius:4px;font-size:11.5px;font-family:inherit;cursor:pointer;transition:all .15s;display:flex;align-items:center;gap:6px}
.mjx-part-btn:hover,.mjx-part-btn[data-on]{border-color:var(--anatomy-lit);color:var(--anatomy-hi);background:color-mix(in srgb,var(--anatomy-lit) 14%,transparent)}
.mjx-part-num{font-weight:700;color:var(--anatomy-lit);font-variant-numeric:tabular-nums}
.mjx-part-swatch{width:8px;height:8px;border-radius:2px;margin-left:auto;flex-shrink:0}
.mjx-inspector{padding:12px 14px;border:1px solid var(--anatomy-lo);border-radius:6px;margin-bottom:12px;background:color-mix(in srgb,var(--anatomy-paper) 95%,var(--anatomy-lit) 5%)}
.mjx-inspector-title{font-size:14px;font-weight:700;color:var(--anatomy-hi);display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}
.mjx-inspector-spec{font-size:11.5px;color:var(--anatomy-lit);font-family:ui-monospace,monospace}
.mjx-inspector-desc{font-size:12.5px;line-height:1.55;color:var(--anatomy-mid);margin-top:6px}
.mjx-piece{transition:opacity .22s;cursor:pointer}
.iso-stage[data-shell="xray"] .mjx-piece[data-piece="body_shell"]{opacity:0.34}
.iso-stage[data-shell="hidden"] .mjx-piece[data-piece="body_shell"]{opacity:0;pointer-events:none}
.iso-stage[data-shell="solid"] .mjx-piece[data-piece="body_shell"]{opacity:0.95}
.iso-stage[data-focus] .mjx-piece:not([data-on]){opacity:0.18 !important}
.iso-stage[data-focus] .mjx-piece[data-on]{opacity:1 !important;filter:drop-shadow(0 0 8px color-mix(in srgb,var(--anatomy-lit) 55%,transparent))}

/* Multi-Material Anodized Color System when data-color-mode="vivid" */
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="chassis"]{
  --anatomy-top:#4b5563;--anatomy-fill:#374151;--anatomy-shade-0:#1f2937;--anatomy-shade-1:#283548;--anatomy-shade-2:#374151;--anatomy-shade-3:#4b5563;--anatomy-hi:#fb923c;--anatomy-mid:#9ca3af;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="drivetrain"]{
  --anatomy-top:#fde68a;--anatomy-fill:#eab308;--anatomy-shade-0:#92400e;--anatomy-shade-1:#b45309;--anatomy-shade-2:#d97706;--anatomy-shade-3:#f59e0b;--anatomy-hi:#fef08a;--anatomy-lit:#facc15;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="motor"]{
  --anatomy-top:#ef4444;--anatomy-fill:#dc2626;--anatomy-shade-0:#7f1d1d;--anatomy-shade-1:#991b1b;--anatomy-shade-2:#b91c1c;--anatomy-shade-3:#ef4444;--anatomy-hi:#38bdf8;--anatomy-mid:#f87171;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="esc"]{
  --anatomy-top:#34d399;--anatomy-fill:#10b981;--anatomy-shade-0:#064e3b;--anatomy-shade-1:#065f46;--anatomy-shade-2:#047857;--anatomy-shade-3:#10b981;--anatomy-hi:#6ee7b7;--anatomy-mid:#34d399;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="battery"]{
  --anatomy-top:#38bdf8;--anatomy-fill:#0284c7;--anatomy-shade-0:#0c4a6e;--anatomy-shade-1:#075985;--anatomy-shade-2:#0369a1;--anatomy-shade-3:#0ea5e9;--anatomy-hi:#facc15;--anatomy-mid:#7dd3fc;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="servo"]{
  --anatomy-top:#f472b6;--anatomy-fill:#db2777;--anatomy-shade-0:#831843;--anatomy-shade-1:#9d174d;--anatomy-shade-2:#be185d;--anatomy-shade-3:#ec4899;--anatomy-hi:#fbcfe8;--anatomy-mid:#f9a8d4;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="suspension_f"],
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="suspension_r"]{
  --anatomy-top:#fb7185;--anatomy-fill:#e11d48;--anatomy-shade-0:#881337;--anatomy-shade-1:#9f1239;--anatomy-shade-2:#be123c;--anatomy-shade-3:#f43f5e;--anatomy-hi:#22d3ee;--anatomy-mid:#fda4af;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="wheels_f"],
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="wheels_r"]{
  --anatomy-top:#facc15;--anatomy-fill:#27272a;--anatomy-shade-0:#18181b;--anatomy-shade-1:#27272a;--anatomy-shade-2:#3f3f46;--anatomy-shade-3:#52525b;--anatomy-hi:#fde047;--anatomy-mid:#a1a1aa;--anatomy-lit:#ef4444;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="upper_deck"]{
  --anatomy-top:#c084fc;--anatomy-fill:#9333ea;--anatomy-shade-0:#581c87;--anatomy-shade-1:#6b21a8;--anatomy-shade-2:#7e22ce;--anatomy-shade-3:#a855f7;--anatomy-hi:#e9d5ff;--anatomy-mid:#d8b4fe;
}
.iso-stage[data-color-mode="vivid"] .mjx-piece[data-piece="body_shell"]{
  --anatomy-top:#f97316;--anatomy-fill:#ea580c;--anatomy-shade-0:#7c2d12;--anatomy-shade-1:#9a3412;--anatomy-shade-2:#c2410c;--anatomy-shade-3:#f97316;--anatomy-hi:#fef08a;--anatomy-mid:#fdba74;--anatomy-lit:#38bdf8;
}

/* Livery 2: WRC Rally Cyan & Championship Gold */
.iso-stage[data-color-mode="vivid"][data-livery="wrc"] .mjx-piece[data-piece="body_shell"]{
  --anatomy-top:#38bdf8;--anatomy-fill:#0284c7;--anatomy-shade-0:#0c4a6e;--anatomy-shade-1:#075985;--anatomy-shade-2:#0284c7;--anatomy-shade-3:#38bdf8;--anatomy-hi:#facc15;--anatomy-lit:#facc15;
}
.iso-stage[data-color-mode="vivid"][data-livery="wrc"] .mjx-piece[data-piece="suspension_f"],
.iso-stage[data-color-mode="vivid"][data-livery="wrc"] .mjx-piece[data-piece="suspension_r"]{
  --anatomy-top:#facc15;--anatomy-fill:#eab308;--anatomy-shade-0:#713f12;--anatomy-shade-1:#a16207;--anatomy-shade-2:#ca8a04;--anatomy-shade-3:#facc15;--anatomy-hi:#38bdf8;
}

/* Livery 3: Carbon Stealth & Acid Lime */
.iso-stage[data-color-mode="vivid"][data-livery="stealth"] .mjx-piece[data-piece="body_shell"]{
  --anatomy-top:#52525b;--anatomy-fill:#27272a;--anatomy-shade-0:#09090b;--anatomy-shade-1:#18181b;--anatomy-shade-2:#27272a;--anatomy-shade-3:#3f3f46;--anatomy-hi:#a3e635;--anatomy-lit:#a3e635;
}
/* Livery 4: Martini Rally Legend (White / Cobalt Blue / Crimson Stripe) */
.iso-stage[data-color-mode="vivid"][data-livery="martini"] .mjx-piece[data-piece="body_shell"]{
  --anatomy-top:#f8fafc;--anatomy-fill:#e2e8f0;--anatomy-shade-0:#475569;--anatomy-shade-1:#94a3b8;--anatomy-shade-2:#cbd5e1;--anatomy-shade-3:#f1f5f9;--anatomy-hi:#ef4444;--anatomy-lit:#2563eb;
}
.iso-stage[data-color-mode="vivid"][data-livery="martini"] .mjx-piece[data-piece="wheels_f"],
.iso-stage[data-color-mode="vivid"][data-livery="martini"] .mjx-piece[data-piece="wheels_r"]{
  --anatomy-top:#f8fafc;--anatomy-fill:#1e293b;--anatomy-hi:#38bdf8;--anatomy-lit:#ef4444;
}

/* Livery 5: Cyber Neon Violet & Cyan */
.iso-stage[data-color-mode="vivid"][data-livery="cyber"] .mjx-piece[data-piece="body_shell"]{
  --anatomy-top:#c084fc;--anatomy-fill:#7e22ce;--anatomy-shade-0:#3b0764;--anatomy-shade-1:#581c87;--anatomy-shade-2:#6b21a8;--anatomy-shade-3:#9333ea;--anatomy-hi:#22d3ee;--anatomy-lit:#22d3ee;
}
.iso-stage[data-color-mode="vivid"][data-livery="cyber"] .mjx-piece[data-piece="drivetrain"],
.iso-stage[data-color-mode="vivid"][data-livery="cyber"] .mjx-piece[data-piece="upper_deck"]{
  --anatomy-top:#22d3ee;--anatomy-fill:#0891b2;--anatomy-hi:#67e8f9;--anatomy-lit:#f472b6;
}
.iso-stage[data-lights="on"] .mjx-headlight-pod{
  filter:drop-shadow(0 0 7px var(--anatomy-lit));
}

@media (max-width:760px){
  .mjx-telemetry{grid-template-columns:repeat(2,1fr)}
  .mjx-scope-bar{grid-template-columns:1fr}
}
`;

const SWATCH_COLORS = {
  chassis: "#fb923c",
  drivetrain: "#facc15",
  motor: "#ef4444",
  esc: "#10b981",
  battery: "#0ea5e9",
  servo: "#ec4899",
  suspension_f: "#f43f5e",
  suspension_r: "#f43f5e",
  wheels_f: "#eab308",
  wheels_r: "#eab308",
  upper_deck: "#a855f7",
  body_shell: "#f97316",
};

const partsButtonsHtml = ORDER.map(
  (id) =>
    `<button type="button" class="mjx-part-btn" data-part-btn="${id}"><span class="mjx-part-num">${PIECES[id].num}</span><span>${PIECES[id].name}</span><span class="mjx-part-swatch" style="background:${SWATCH_COLORS[id]}"></span></button>`,
).join("");

const customControlsHtml = `
<div class="mjx-topbar">
  <div class="mjx-topbar-group">
    <span class="mjx-topbar-label">🎬 动态演示剧本 (Auto Demo Scenarios):</span>
    <button type="button" class="mjx-btn" data-demo="manual" data-active>🕹️ 自由操控台</button>
    <button type="button" class="mjx-btn" data-demo="launch">🚀 3S 弹射起步 (62km/h)</button>
    <button type="button" class="mjx-btn" data-demo="drift">🌀 拉力钟摆漂移 + 陀螺仪救车</button>
    <button type="button" class="mjx-btn" data-demo="offroad">⛰️ 砂石飞跳与油压避震</button>
    <button type="button" class="mjx-btn" data-demo="tour">🔍 12 总成自动拆解巡礼</button>
  </div>
  <div class="mjx-topbar-group">
    <span class="mjx-topbar-label">🎨 涂装与分色:</span>
    <button type="button" class="mjx-btn" data-livery-btn="hyper" data-active>厂队赤红金</button>
    <button type="button" class="mjx-btn" data-livery-btn="wrc">WRC 蓝金拉力</button>
    <button type="button" class="mjx-btn" data-livery-btn="martini">传奇红白蓝</button>
    <button type="button" class="mjx-btn" data-livery-btn="cyber">赛博霓虹紫</button>
    <button type="button" class="mjx-btn" data-livery-btn="stealth">黑金暗夜绿</button>
    <button type="button" class="mjx-btn" data-livery-btn="mono">工程单色</button>
  </div>
</div>
<div class="mjx-toolbar">
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>整车拆解与车壳透视</span><kbd>E / S / B</kbd></div>
    <div class="mjx-btn-row">
      <button type="button" class="mjx-btn" data-act="explode">爆炸拆解 (E)</button>
      <button type="button" class="mjx-btn" data-act="bump">飞跳下压 (S)</button>
      <button type="button" class="mjx-btn" data-act="shell">车壳: X-Ray 透视 (B)</button>
      <button type="button" class="mjx-btn" data-act="lights" data-active>💡 车灯 ON (L)</button>
      <button type="button" class="mjx-btn" data-act="gyro" data-active>G3C 陀螺仪 ON</button>
    </div>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>锂电倍率与电压 (LiPo)</span><span data-bat-label>2S · 7.4V</span></div>
    <div class="mjx-btn-row">
      <button type="button" class="mjx-btn" data-bat="2" data-active>2S 7.4V (43km/h)</button>
      <button type="button" class="mjx-btn" data-bat="3">3S 11.1V (狂暴 62km/h)</button>
    </div>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>2845 无刷油门 (Throttle)</span><span data-thr-val>35%</span></div>
    <input type="range" class="mjx-slider" data-thr min="0" max="100" value="35" aria-label="Throttle percentage"/>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>阿克曼转向 / 钟摆角 (Steer)</span><span data-str-val>0°</span></div>
    <input type="range" class="mjx-slider" data-str min="-28" max="28" value="0" aria-label="Steering angle degrees"/>
  </div>
</div>
<div class="mjx-telemetry">
  <div class="mjx-stat">
    <div class="mjx-stat-label">2845 无刷电机转速 (Motor)</div>
    <div class="mjx-stat-val" data-tel-motor>9,583 RPM</div>
  </div>
  <div class="mjx-stat">
    <div class="mjx-stat-label">四驱轮端转速 (FDR 8.54:1)</div>
    <div class="mjx-stat-val" data-tel-wheel>928 RPM</div>
  </div>
  <div class="mjx-stat">
    <div class="mjx-stat-label">测功台实时车速 (Speed)</div>
    <div class="mjx-stat-val" data-lit data-tel-speed>15.0 km/h</div>
  </div>
  <div class="mjx-stat">
    <div class="mjx-stat-label">阿克曼内/外轮角 & 陀螺仪修正</div>
    <div class="mjx-stat-val" data-tel-steer>0.0° / 0.0° · Gyro 0°</div>
  </div>
  <div class="mjx-stat">
    <div class="mjx-stat-label">车身姿态 (俯仰 Pitch / 避震 Travel)</div>
    <div class="mjx-stat-val" data-tel-pose>Pitch +0.4° · 0.0 mm</div>
  </div>
</div>
<div class="mjx-scope-bar">
  <canvas id="mjxScope" class="mjx-scope-canvas" width="680" height="76"></canvas>
  <div class="mjx-scope-legend">
    <div style="font-weight:700;color:var(--anatomy-hi)">📈 实时多通道动力学示波器 (60Hz)</div>
    <div class="mjx-scope-item"><span class="mjx-dot" style="background:#facc15"></span><span>车速曲线 Speed (0–65 km/h)</span></div>
    <div class="mjx-scope-item"><span class="mjx-dot" style="background:#38bdf8"></span><span>油压绞牙避震行程 Shock Travel (mm)</span></div>
    <div class="mjx-scope-item"><span class="mjx-dot" style="background:#34d399"></span><span>G3C 陀螺仪反打角 Gyro Counter (°)</span></div>
  </div>
</div>
`;

const inspectorHtml = `
<div class="mjx-inspector" data-inspector>
  <div class="mjx-inspector-title">
    <span data-ins-name>02 · 4WD 中央金属主轴 & 前后行星伞齿差速器 (4WD Center Shaft & Planetary Bevel Diffs)</span>
    <span class="mjx-inspector-spec" data-ins-spec>FDR 8.54:1 · 15T/45T 钢齿 · 37T/13T 粉末冶金伞齿 + 4 星齿轮差速器</span>
  </div>
  <div class="mjx-inspector-desc" data-ins-desc>${PIECES.drivetrain.principle}</div>
</div>
<div class="mjx-parts-grid">${partsButtonsHtml}</div>
`;

const navBannerHtml = `<div style="max-width:1020px;margin:10px auto 6px;padding:8px 14px;display:flex;justify-content:space-between;align-items:center;font-family:system-ui,-apple-system,sans-serif;font-size:12.5px;border-radius:8px;background:rgba(128,128,128,0.12);border:1px solid rgba(128,128,128,0.22)">
  <a href="../../index.html" style="color:inherit;text-decoration:none;font-weight:600">← 返回 AI Agent Skills &amp; REA 演示门户 (Portal)</a>
  <div style="display:flex;gap:8px;align-items:center">
    <span style="opacity:0.7">整车 12 总成 + 5 动态演示:</span>
    <a href="index.html" style="padding:3px 9px;border-radius:4px;text-decoration:none;${theme === "dark" ? "background:#f5a524;color:#111;font-weight:700;" : "color:inherit;border:1px solid rgba(128,128,128,0.35);"}">🌙 暗黑多彩测功台 (Dark)</a>
    <a href="mjx-14303-chassis-light.html" style="padding:3px 9px;border-radius:4px;text-decoration:none;${theme === "light" ? "background:#d97706;color:#fff;font-weight:700;" : "color:inherit;border:1px solid rgba(128,128,128,0.35);"}">☀️ 工程浅色蓝图 (Light)</a>
  </div>
</div>`;

const body = `<style>${CSS}</style>${navBannerHtml}<div class="mjx-wrap">${k.plateHtml({
  fig: "Fig 1 · MJX HYPER GO 14303 · 12-ASSEMBLY COMPLETE VEHICLE LAB",
  title: "美嘉欣 14303 · 1/14 全时四驱无刷拉力/漂移整车机械原理与动态测功台",
  hint: "支持 5 种自动动态剧本 · 4 套阳极氧化分色涂装 · 按 E 爆炸拆解 · 按 B 切换车壳透视",
  readout: "2S 7.4V · 15.0 km/h · Manual Lab",
  keys: [
    { mark: "lit", label: "核心动力链：2845 无刷电机 → 15T/45T 金属齿 → 中央铝轴 → 前后 37T/13T 行星伞齿差速器 → 四轮 CVD + 通风刹车盘" },
    { mark: "raised", label: "12 大整车机械总成（含可透视拉力宽体车壳、双层尾翼、CNC 二楼板与前后防倾杆，点击独立检视）" },
  ],
  caption:
    inspectorHtml +
    "美嘉欣（MJX）Hyper Go 14303 采用 192 mm 轴距 6061-T6 铝合金蜂窝主底盘与 CNC 二楼板抗扭强化结构。2845 3700KV 四极无刷电机输出动力经初级齿轮副（45T/15T = 3.0）与前后粉末冶金行星伞齿差速器（37T/13T = 2.846，总减速比 8.54:1）分配至四轮；配备前后横向防倾杆、油压绞牙独立悬架、内置 G3C 陀螺仪的 17g 数字舵机阿克曼转向系统及高下压力拉力宽体车壳。",
  body: `<div class="iso-stage" data-color-mode="vivid" data-livery="hyper" data-shell="xray" data-lights="on" tabindex="0" role="application" aria-label="美嘉欣 14303 整车互动解剖与动态测功台">${svg}</div>${customControlsHtml}`,
})}</div>`;

const live = `
const P = ${JSON.stringify(P)};
const PIECES = ${JSON.stringify(PIECES)};
const ORDER = ${JSON.stringify(ORDER)};
const stage = document.querySelector(".iso-stage");
const svg = stage.querySelector("svg");
const readout = document.querySelector("[data-readout]");
const pieceEls = [...svg.querySelectorAll(".mjx-piece")];
const partBtns = [...document.querySelectorAll("[data-part-btn]")];
const demoBtns = [...document.querySelectorAll("[data-demo]")];
const liveryBtns = [...document.querySelectorAll("[data-livery-btn]")];
const btnExplode = document.querySelector('[data-act="explode"]');
const btnBump = document.querySelector('[data-act="bump"]');
const btnShell = document.querySelector('[data-act="shell"]');
const btnLights = document.querySelector('[data-act="lights"]');
const btnGyro = document.querySelector('[data-act="gyro"]');
const batBtns = [...document.querySelectorAll("[data-bat]")];
const thrInput = document.querySelector("[data-thr]");
const strInput = document.querySelector("[data-str]");
const thrVal = document.querySelector("[data-thr-val]");
const strVal = document.querySelector("[data-str-val]");
const batLabel = document.querySelector("[data-bat-label]");
const telMotor = document.querySelector("[data-tel-motor]");
const telWheel = document.querySelector("[data-tel-wheel]");
const telSpeed = document.querySelector("[data-tel-speed]");
const telSteer = document.querySelector("[data-tel-steer]");
const telPose = document.querySelector("[data-tel-pose]");
const insName = document.querySelector("[data-ins-name]");
const insSpec = document.querySelector("[data-ins-spec]");
const insDesc = document.querySelector("[data-ins-desc]");
const torqueLine = svg.querySelector(".mjx-torque-line");
const aeroLines = [...svg.querySelectorAll(".mjx-aero-line")];
const dynoFlows = [...svg.querySelectorAll(".mjx-dyno-flow")];
const frontLeftWheel = svg.querySelector('[data-wheel="front-l"]');
const frontRightWheel = svg.querySelector('[data-wheel="front-r"]');
const rearLeftWheel = svg.querySelector('[data-wheel="rear-l"]');
const rearRightWheel = svg.querySelector('[data-wheel="rear-r"]');
const wheelSpokes = [...svg.querySelectorAll(".mjx-wheel-spokes")];
const fanBlades = svg.querySelector(".mjx-fan-blades");
const scopeCanvas = document.getElementById("mjxScope");
const scopeCtx = scopeCanvas ? scopeCanvas.getContext("2d") : null;

const KV = 3700;
const PINION = 15, SPUR = 45;
const DIFF_RING = 37, DIFF_PINION = 13;
const FDR = (SPUR / PINION) * (DIFF_RING / DIFF_PINION);
const TIRE_DIAM_M = 0.058;
const LOAD_EFF = 0.826;

let cells = 2;
let throttle = 0.35;
let steerDeg = 0;
let gyroEnabled = true;
let apart = false;
let shellMode = "xray"; // "xray" | "solid" | "hidden"
let demoMode = "manual"; // "manual" | "launch" | "drift" | "offroad" | "tour"
let demoStart = 0;
let selected = null;
let clock = 0;
let last = 0;
let wheelPhase = 0;

const springs = Object.fromEntries(ORDER.map((id) => [id, { x: 0, v: 0, target: 0 }]));
const bumpState = { z: 0, v: 0 };
const history = [];

function setCells(n) {
  cells = n;
  for (const b of batBtns) {
    if (Number(b.dataset.bat) === n) b.setAttribute("data-active", "");
    else b.removeAttribute("data-active");
  }
  batLabel.textContent = cells === 3 ? "3S · 11.1V" : "2S · 7.4V";
}

function setThrottle(val) {
  throttle = Math.max(0, Math.min(1, val));
  thrInput.value = String(Math.round(throttle * 100));
  thrVal.textContent = Math.round(throttle * 100) + "%";
}

function setSteer(deg) {
  steerDeg = Math.max(-28, Math.min(28, Math.round(deg)));
  strInput.value = String(steerDeg);
  strVal.textContent = (steerDeg > 0 ? "+" : "") + steerDeg + "°";
}

function selectPart(id, forceKeep) {
  selected = forceKeep ? id : (selected === id ? null : id);
  if (selected && PIECES[selected]) {
    stage.setAttribute("data-focus", "");
    const info = PIECES[selected];
    insName.textContent = info.num + " · " + info.name + " (" + info.en + ")";
    insSpec.textContent = info.spec + " · [" + info.colorTag + "]";
    insDesc.textContent = info.principle;
  } else {
    selected = null;
    stage.removeAttribute("data-focus");
    const info = PIECES.drivetrain;
    insName.textContent = info.num + " · " + info.name + " (" + info.en + ")";
    insSpec.textContent = info.spec + " · [" + info.colorTag + "]";
    insDesc.textContent = info.principle;
  }
  for (const el of pieceEls) {
    if (selected && el.dataset.piece === selected) el.setAttribute("data-on", "");
    else el.removeAttribute("data-on");
  }
  for (const btn of partBtns) {
    if (selected && btn.dataset.partBtn === selected) btn.setAttribute("data-on", "");
    else btn.removeAttribute("data-on");
  }
}

function toggleExplode(force) {
  apart = typeof force === "boolean" ? force : !apart;
  if (apart) btnExplode.setAttribute("data-active", "");
  else btnExplode.removeAttribute("data-active");
  ORDER.forEach((id) => {
    springs[id].target = apart ? 1 : 0;
  });
}

function cycleShell(forceMode) {
  const modes = ["xray", "solid", "hidden"];
  shellMode = forceMode || modes[(modes.indexOf(shellMode) + 1) % modes.length];
  stage.setAttribute("data-shell", shellMode);
  const labels = { xray: "车壳: X-Ray 透视 (B)", solid: "车壳: 实心涂装 (B)", hidden: "车壳: 隐藏裸底盘 (B)" };
  btnShell.textContent = labels[shellMode];
}

function triggerBump(impulse = -175) {
  bumpState.v = impulse;
  btnBump.setAttribute("data-active", "");
  setTimeout(() => btnBump.removeAttribute("data-active"), 360);
}

function setDemoMode(mode) {
  demoMode = mode;
  demoStart = clock;
  for (const b of demoBtns) {
    if (b.dataset.demo === mode) b.setAttribute("data-active", "");
    else b.removeAttribute("data-active");
  }
  if (mode === "manual") {
    if (selected) selectPart(null);
  } else if (mode === "launch") {
    toggleExplode(false);
    setCells(3);
    setSteer(0);
    if (selected) selectPart(null);
  } else if (mode === "drift") {
    toggleExplode(false);
    setCells(3);
    gyroEnabled = true;
    btnGyro.setAttribute("data-active", "");
    btnGyro.textContent = "G3C 陀螺仪 ON";
    if (selected) selectPart(null);
  } else if (mode === "offroad") {
    toggleExplode(false);
    setCells(2);
    setThrottle(0.68);
    if (selected) selectPart(null);
  } else if (mode === "tour") {
    toggleExplode(true);
    cycleShell("xray");
  }
}

for (const b of demoBtns) {
  b.addEventListener("click", () => setDemoMode(b.dataset.demo));
}

for (const b of liveryBtns) {
  b.addEventListener("click", () => {
    const liv = b.dataset.liveryBtn;
    for (const other of liveryBtns) {
      if (other === b) other.setAttribute("data-active", "");
      else other.removeAttribute("data-active");
    }
    if (liv === "mono") {
      stage.setAttribute("data-color-mode", "mono");
    } else {
      stage.setAttribute("data-color-mode", "vivid");
      stage.setAttribute("data-livery", liv);
    }
  });
}

for (const el of pieceEls) {
  el.addEventListener("click", (e) => {
    e.stopPropagation();
    selectPart(el.dataset.piece);
  });
}
stage.addEventListener("click", () => {
  if (selected) selectPart(null);
});
for (const btn of partBtns) {
  btn.addEventListener("click", () => selectPart(btn.dataset.partBtn));
}

btnExplode.addEventListener("click", () => toggleExplode());
btnBump.addEventListener("click", () => triggerBump(-185));
btnShell.addEventListener("click", () => cycleShell());
if (btnLights) {
  btnLights.addEventListener("click", () => {
    const isOn = stage.getAttribute("data-lights") !== "off";
    stage.setAttribute("data-lights", isOn ? "off" : "on");
    if (!isOn) btnLights.setAttribute("data-active", "");
    else btnLights.removeAttribute("data-active");
    btnLights.textContent = !isOn ? "💡 车灯 ON (L)" : "💡 车灯 OFF (L)";
  });
}
btnGyro.addEventListener("click", () => {
  gyroEnabled = !gyroEnabled;
  if (gyroEnabled) btnGyro.setAttribute("data-active", "");
  else btnGyro.removeAttribute("data-active");
  btnGyro.textContent = gyroEnabled ? "G3C 陀螺仪 ON" : "G3C 陀螺仪 OFF";
});

for (const b of batBtns) {
  b.addEventListener("click", () => setCells(Number(b.dataset.bat)));
}

thrInput.addEventListener("input", () => {
  if (demoMode !== "manual") setDemoMode("manual");
  setThrottle(Number(thrInput.value) / 100);
});

strInput.addEventListener("input", () => {
  if (demoMode !== "manual") setDemoMode("manual");
  setSteer(Number(strInput.value));
});

window.addEventListener("keydown", (e) => {
  if (e.key === "e" || e.key === "E") {
    e.preventDefault();
    toggleExplode();
  } else if (e.key === "s" || e.key === "S") {
    e.preventDefault();
    triggerBump(-185);
  } else if (e.key === "b" || e.key === "B") {
    e.preventDefault();
    cycleShell();
  } else if (e.key === "l" || e.key === "L") {
    e.preventDefault();
    if (btnLights) btnLights.click();
  } else if (e.key === "ArrowLeft") {
    setDemoMode("manual");
    setSteer(steerDeg - 4);
  } else if (e.key === "ArrowRight") {
    setDemoMode("manual");
    setSteer(steerDeg + 4);
  }
});

function drawOscilloscope() {
  if (!scopeCtx || !scopeCanvas) return;
  const w = scopeCanvas.width;
  const h = scopeCanvas.height;
  scopeCtx.clearRect(0, 0, w, h);

  // Subtle grid lines
  scopeCtx.strokeStyle = "rgba(148, 163, 184, 0.16)";
  scopeCtx.lineWidth = 1;
  for (let y = 18; y < h; y += 20) {
    scopeCtx.beginPath();
    scopeCtx.moveTo(0, y);
    scopeCtx.lineTo(w, y);
    scopeCtx.stroke();
  }

  if (history.length < 2) return;

  // Plot Speed (0..65 km/h -> bottom to top)
  scopeCtx.strokeStyle = "#facc15";
  scopeCtx.lineWidth = 2;
  scopeCtx.beginPath();
  history.forEach((pt, idx) => {
    const x = (idx / 160) * w;
    const y = h - 8 - (Math.min(65, pt.speed) / 65) * (h - 16);
    if (idx === 0) scopeCtx.moveTo(x, y);
    else scopeCtx.lineTo(x, y);
  });
  scopeCtx.stroke();

  // Plot Shock Travel (-12..+12 mm centered at h/2)
  scopeCtx.strokeStyle = "#38bdf8";
  scopeCtx.lineWidth = 1.8;
  scopeCtx.beginPath();
  history.forEach((pt, idx) => {
    const x = (idx / 160) * w;
    const y = h * 0.5 - (pt.shock / 12) * (h * 0.38);
    if (idx === 0) scopeCtx.moveTo(x, y);
    else scopeCtx.lineTo(x, y);
  });
  scopeCtx.stroke();

  // Plot Gyro Counter-Steer (-18..+18 deg centered at h/2)
  scopeCtx.strokeStyle = "#34d399";
  scopeCtx.lineWidth = 1.6;
  scopeCtx.beginPath();
  history.forEach((pt, idx) => {
    const x = (idx / 160) * w;
    const y = h * 0.5 - (pt.gyro / 18) * (h * 0.38);
    if (idx === 0) scopeCtx.moveTo(x, y);
    else scopeCtx.lineTo(x, y);
  });
  scopeCtx.stroke();
}

function tick(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 24) : 1 / 60;
  last = now;
  clock += dt;
  const elapsed = clock - demoStart;

  // Automated Demo Scenarios
  if (demoMode === "launch") {
    const cycle = elapsed % 5.5;
    if (cycle < 0.7) {
      setThrottle(0.08);
    } else if (cycle < 3.8) {
      const ramp = Math.min(1, (cycle - 0.7) / 0.65);
      setThrottle(0.15 + ramp * 0.85);
    } else {
      setThrottle(Math.max(0.1, 1 - (cycle - 3.8) * 0.6));
    }
  } else if (demoMode === "drift") {
    setThrottle(0.78);
    const wave = Math.sin(elapsed * 2.1) * 25;
    setSteer(wave);
  } else if (demoMode === "offroad") {
    setThrottle(0.65 + Math.sin(elapsed * 1.7) * 0.18);
    setSteer(Math.sin(elapsed * 1.3) * 10);
    // Periodic gravel washboard & jump impulse
    if (Math.sin(elapsed * 11) > 0.92 && Math.abs(bumpState.z) < 2.2) {
      bumpState.v -= 48;
    }
    if (Math.floor((elapsed - dt) / 2.6) < Math.floor(elapsed / 2.6)) {
      triggerBump(-210);
    }
  } else if (demoMode === "tour") {
    setThrottle(0.42);
    const idx = Math.floor(elapsed / 2.8) % ORDER.length;
    const targetPart = ORDER[idx];
    if (selected !== targetPart) {
      selectPart(targetPart, true);
    }
  }

  for (const id of ORDER) {
    const s = springs[id];
    const stiff = 78, damp = 15;
    s.v += ((s.target - s.x) * stiff - s.v * damp) * dt;
    s.x += s.v * dt;
  }
  bumpState.v += (-bumpState.z * 210 - bumpState.v * 18) * dt;
  bumpState.z += bumpState.v * dt;

  const voltage = cells * 3.7;
  const motorRpm = Math.round(voltage * KV * throttle);
  const wheelRpm = Math.round((motorRpm / FDR) * LOAD_EFF);
  const speedKmh = (wheelRpm * Math.PI * TIRE_DIAM_M * 60) / 1000;

  const gyroCounter =
    gyroEnabled && (throttle > 0.2 || Math.abs(steerDeg) > 4)
      ? Math.sin(clock * 5.2) * (throttle * 5.8) - steerDeg * 0.36
      : 0;
  const netSteer = steerDeg + gyroCounter;
  const innerDeg = netSteer * 1.08;
  const outerDeg = netSteer * 0.84;

  // Dynamic Pitch (Launch Squat under high throttle) & Roll (under steering lateral G)
  const squatPitchDeg = throttle > 0.45 ? (throttle - 0.45) * (cells === 3 ? 4.2 : 2.4) : 0;
  const frontLiftZ = squatPitchDeg * 0.65;
  const rearSquatZ = -squatPitchDeg * 0.95;

  wheelPhase += dt * (wheelRpm / 60) * Math.PI * 2;

  for (const el of pieceEls) {
    const id = el.dataset.piece;
    const [mx, my, mz] = el.dataset.move.split(",").map(Number);
    const share = springs[id].x;
    let dz = mz * share;
    if (id === "chassis" || id === "drivetrain" || id === "motor" || id === "esc" || id === "battery" || id === "servo" || id === "upper_deck" || id === "body_shell") {
      dz += bumpState.z * 0.58 + (frontLiftZ + rearSquatZ) * 0.5;
    } else if (id === "suspension_f") {
      dz += bumpState.z * 0.86 + frontLiftZ;
    } else if (id === "suspension_r") {
      dz += bumpState.z * 0.86 + rearSquatZ;
    }
    el.setAttribute("transform", translateAlong(P, [mx * share, my * share, dz]));
  }

  // Front wheel Ackermann steering + high-frequency road vibration
  const roadJitter = throttle > 0.05 ? Math.sin(clock * 38) * (throttle * 0.45) : 0;
  if (frontLeftWheel && frontRightWheel) {
    const shiftL = (netSteer / 28) * 4.2;
    const shiftR = (netSteer / 28) * 4.2;
    frontLeftWheel.setAttribute("transform", translateAlong(P, [shiftL, shiftL * 0.65, roadJitter]));
    frontRightWheel.setAttribute("transform", translateAlong(P, [-shiftR, shiftR * 0.65, -roadJitter]));
  }
  if (rearLeftWheel && rearRightWheel) {
    rearLeftWheel.setAttribute("transform", translateAlong(P, [0, 0, -roadJitter]));
    rearRightWheel.setAttribute("transform", translateAlong(P, [0, 0, roadJitter]));
  }

  // Wheel spoke & cooling fan visual pulse
  const spokePulse = 0.55 + 0.45 * Math.sin(wheelPhase);
  for (const sp of wheelSpokes) {
    sp.style.opacity = throttle > 0.02 ? spokePulse.toFixed(2) : "1";
  }
  if (fanBlades) {
    fanBlades.style.opacity = (0.45 + 0.55 * Math.cos(wheelPhase * 2.5)).toFixed(2);
  }

  const flowDur = throttle > 0.02 ? Math.max(0.14, 0.92 - throttle * 0.76).toFixed(2) + "s" : "0s";
  if (torqueLine) {
    torqueLine.style.animationDuration = flowDur;
    torqueLine.style.opacity = throttle > 0.02 ? "1" : "0.25";
  }
  for (const al of aeroLines) {
    al.style.animationDuration = flowDur;
    al.style.opacity = throttle > 0.15 && shellMode !== "hidden" ? Math.min(0.95, throttle).toFixed(2) : "0";
  }
  for (const df of dynoFlows) {
    df.style.animationDuration = flowDur;
    df.style.opacity = throttle > 0.05 ? Math.min(0.85, 0.2 + throttle * 0.7).toFixed(2) : "0.15";
  }

  telMotor.textContent = motorRpm.toLocaleString("en-US") + " RPM";
  telWheel.textContent = wheelRpm.toLocaleString("en-US") + " RPM";
  telSpeed.textContent = speedKmh.toFixed(1) + " km/h";
  telSteer.textContent =
    innerDeg.toFixed(1) + "° / " + outerDeg.toFixed(1) + "° · Gyro " + (gyroCounter >= 0 ? "+" : "") + gyroCounter.toFixed(1) + "°";
  telPose.textContent =
    "Pitch +" + squatPitchDeg.toFixed(1) + "° · " + (bumpState.z + rearSquatZ).toFixed(1) + " mm";

  const modeNames = {
    manual: "Manual Lab",
    launch: "3S Launch Squat",
    drift: "Rally Drift + Gyro",
    offroad: "Gravel Jump",
    tour: "12-Part Tour",
  };
  const stateLabel = apart
    ? "Exploded (12 Assemblies)"
    : Math.abs(bumpState.z) > 0.4
      ? "Shock " + bumpState.z.toFixed(1) + " mm"
      : modeNames[demoMode];
  const rText = cells + "S " + voltage.toFixed(1) + "V · " + speedKmh.toFixed(1) + " km/h · " + stateLabel;
  if (readout.textContent !== rText) readout.textContent = rText;

  history.push({ speed: speedKmh, shock: bumpState.z + rearSquatZ, gyro: gyroCounter });
  if (history.length > 160) history.shift();
  drawOscilloscope();

  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
`;

const htmlContent = k.pageHtml({
  title: "MJX Hyper Go 14303 · 1/14 4WD 整车机械解剖与动态测功台",
  theme,
  body,
  script: kitScript() + live,
  width: 1020,
});
const outFile = join(HERE, theme === "light" ? "mjx-14303-chassis-light.html" : "mjx-14303-chassis.html");
writeFileSync(outFile, htmlContent);
console.log("wrote", outFile);
if (theme !== "light") {
  const indexOut = join(HERE, "index.html");
  writeFileSync(indexOut, htmlContent);
  console.log("wrote", indexOut);
}

if (runAudit) {
  A.auditOrExit(R, P, { step: 1.0, clearanceStep: 1.0, cover: ["*"] });
}

