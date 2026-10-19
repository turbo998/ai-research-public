import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../kit/iso-kit.mjs";
import * as G from "../../kit/lathe.mjs";
import { tubePieces, tubeSvg } from "../../kit/tube.mjs";
import * as A from "../../kit/audit.mjs";
import { kitScript } from "../../scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";
const runAudit = process.argv.includes("--audit");

const WIDTH = 920;
const HEIGHT = 560;

// World coordinate system:
// x: longitudinal axis (-135 front bumper -> +135 rear bumper; 192 units wheelbase: front axle x = -84, rear axle x = +84)
// y: lateral axis (-62 left wheel -> +62 right wheel; 125 units track width)
// z: vertical axis (0 chassis bottom reference)
const BENCH = { x: -168, y: -102, w: 336, d: 204, r: 10 };
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
    [-145, -80, 118],
    [145, 80, 118],
  ],
  WIDTH,
  HEIGHT,
  { pad: 24, azimuth: 41, elevation: 29 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const depth = (x, y, z = 0) => k.depthOf([x, y, z], P);

// 10 Mechanical Sub-Assemblies of MJX Hyper Go 14303 (1/14 4WD Rally/Drift Chassis)
const PIECES = {
  chassis: {
    num: "01",
    name: "6061-T6 铝合金底盘 & 防撞总成",
    en: "6061-T6 Alu Chassis & Bumpers",
    spec: "192 mm 轴距 · 2.0 mm 阳极氧化铝板 · 高密度 EVA 前防撞",
    principle:
      "整车承载基座。采用 6061-T6 铝合金 CNC 冲压折弯成型，提供极高抗扭刚度并兼作全车散热底板；前端配备宽体高吸能 EVA 海绵防撞与防尘护板定位槽，抵御高速拉力碰撞。",
    move: [0, 0, -14],
  },
  drivetrain: {
    num: "02",
    name: "4WD 中央金属轴与前后伞齿差速器",
    en: "4WD Center Shaft & Metal Bevel Diffs",
    spec: "FDR 8.54:1 · 15T/45T 金属主齿 · 37T/13T 粉末冶金伞齿差速器",
    principle:
      "【核心焦点总成】全时四驱刚性动力链：2845 无刷电机带动 15T 钢制马达齿驱动 45T 大齿（初级减速 3.0:1），经贯通前后的高强度铝合金中央传动轴与前后 37T/13T 金属行星齿轮差速器（次级减速 2.846:1），由金属 CVD 狗骨分配至四轮。",
    move: [0, 0, 26],
  },
  motor: {
    num: "03",
    name: "2845 3700KV 四极无刷电机 & 散热风扇",
    en: "2845 3700KV 4-Pole Brushless Motor",
    spec: "3700 KV · 2S 27,380 RPM / 3S 41,070 RPM · 铝合金鳍片散热 + 涡轮风扇",
    principle:
      "中后置偏右布局的四极无感无刷电机，搭配阳极氧化多鳍片铝合金散热座与顶部 14,000 RPM 主动冷却风扇。在 2S (7.4V) 下极速 42.8 km/h，接入 3S (11.1V) 锂电可爆发 62.4 km/h 狂暴极速。",
    move: [18, 28, 48],
  },
  esc: {
    num: "04",
    name: "E45R 45A 独立无刷电调 & G3C 陀螺仪接收机",
    en: "45A Brushless ESC & G3C Gyro Receiver",
    spec: "45A 持续电流 · 支持 2S/3S LiPo · 内置 G3C 车身横摆角速度陀螺仪",
    principle:
      "防泼水 45A 独立无刷电子调速器通过三相硅胶线（U/V/W）高频换相驱动电机；独立接收机内置 G3C 压电陀螺仪，实时检测漂移甩尾角速度并自动向 17g 舵机叠加反打修正指令（Counter-steer）。",
    move: [-14, -32, 52],
  },
  battery: {
    num: "05",
    name: "2S/3S 高倍率锂电池仓与快速锁扣",
    en: "2S 7.4V / 3S 11.1V Li-ion/LiPo Pack",
    spec: "标配 7.4V 2000mAh 15C · 兼容 11.1V 3S · 纵向平衡配重仓",
    principle:
      "位于底盘左侧纵向布置，与右侧电机+舵机形成精准的左右 50:50 动态配重平衡，降低高速过弯侧倾；顶部快拆防松压板固定。",
    move: [22, -38, 44],
  },
  servo: {
    num: "06",
    name: "17g 金属齿数字舵机 & 双摇臂阿克曼转向",
    en: "17g Digital Servo & Dual-Bellcrank Ackermann",
    spec: "2.4 kg·cm 扭矩 · 0.11s/60° · 内置弹簧舵机保 (Servo Saver)",
    principle:
      "17g 高速数字舵机通过可调拉杆推动中央双摇臂转向机构（Dual-Bellcrank）。主摇臂内置高刚度缓冲弹簧（Servo Saver），前轮撞击路肩时自动卸力保护舵机齿；几何关系满足阿克曼转角（内轮转角 > 外轮转角）。",
    move: [-18, 34, 42],
  },
  suspension_f: {
    num: "07",
    name: "前独立双叉臂悬架 & 油压绞牙金属避震",
    en: "Front Double-Wishbone & Oil-Filled Coilovers",
    spec: "CNC 金属蝴蝶架 · 金属油压筒身 · 预载可调螺旋弹簧 · 14 mm 行程",
    principle:
      "上下 A 臂（双叉臂）独立悬架配合倾角拉杆，保证车轮跳动时接地倾角稳定；两支充油金属绞牙避震器倾斜安装于前铝合金蝴蝶架（Shock Tower），吸收高频颠簸并抑制抬头/点头。",
    move: [-58, 0, 56],
  },
  suspension_r: {
    num: "08",
    name: "后独立双叉臂悬架 & 后油压绞牙金属避震",
    en: "Rear Double-Wishbone & Oil-Filled Coilovers",
    spec: "后金属蝴蝶架 · 渐进式螺旋弹簧 · 防倾杆预留孔位",
    principle:
      "后双叉臂悬架连接后轮轴座（Hub Carrier）与后差速器箱体，后油压金属绞牙避震器提供出弯加速时的车尾下蹲支撑（Squat Control），提升拉力砂石路面抓地力。",
    move: [58, 0, 56],
  },
  wheels_f: {
    num: "09",
    name: "前 58mm 拉力轮胎 & 金属转向杯总成",
    en: "Front 58mm Rally/Drift Wheels & Knuckles",
    spec: "Ø58 × 24 mm · 12 mm 六角金属结合器 · 全车滚珠轴承",
    principle:
      "前轮安装在带双滚珠轴承的转向杯（Steering Knuckle）上，由万向节金属 CVD 传动轴驱动，在实现 ±28° 大角度转向与陀螺仪反打的同时无动力干涉。",
    move: [-64, 46, 12],
  },
  wheels_r: {
    num: "10",
    name: "后 58mm 拉力轮胎 & 后轮座总成",
    en: "Rear 58mm Rally/Drift Wheels & Hubs",
    spec: "Ø58 × 24 mm · 1.5° 固定内束角 (Toe-in) · 高耐磨橡胶/POM 漂移胎套",
    principle:
      "后轮座预设 1.5° 内束角（Toe-in）以增强直线加速与出弯稳定性；可一键更换高抓地橡胶拉力胎或硬质 POM 漂移胎环。",
    move: [64, 46, 12],
  },
};

const ORDER = [
  "chassis",
  "drivetrain",
  "motor",
  "esc",
  "battery",
  "servo",
  "suspension_f",
  "suspension_r",
  "wheels_f",
  "wheels_r",
];

// Build bench plate (stationary reference surface with millimeter scale)
function buildBench() {
  const out = [`<path class="iso-halo" d="${k.haloOf(BENCH, BENCH_Z - FOOT_H, BENCH_H, P)}"/>`];
  for (const [x, y] of k.corners(BENCH, 22).sort((a, b) => depth(...a) - depth(...b))) {
    out.push(S(k.cylinder(x, y, 7.5, BENCH_Z - FOOT_H, 1.8, P, 24), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 5.6, BENCH_Z - FOOT_H + 1.8, FOOT_H - 1.8, P, 24), { tone: "mid" }));
  }
  out.push(S(k.slabOf(BENCH, BENCH_Z, BENCH_H, P, 8, 1.5), { tone: "lo" }));
  out.push(L(k.planOutline(k.insetPlan(BENCH, 6), BENCH_Z + BENCH_H, P), { tone: "faint" }));
  const zTop = BENCH_Z + BENCH_H;

  // Center chassis standoffs supporting the 14303 chassis so wheels can spin freely
  for (const [sx, sy] of [[-48, -18], [-48, 18], [48, -18], [48, 18]]) {
    out.push(S(k.cylinder(sx, sy, 4.2, zTop, CHASSIS_Z - zTop, P, 20), { tone: "lo" }));
  }

  // Wheelbase ruler strip along front edge of bench
  const strip = { x: -116, y: BENCH.y + BENCH.d - 16, w: 232, d: 8, r: 1.2 };
  out.push(S(k.slabOf(strip, zTop, 0.7, P, 3), { tone: "mid", crease: "none" }));
  const ticks = k.topTicks(AXLE_F, AXLE_R, 6, 4, strip.y + 1, zTop + 0.7, [2.2, 4.2], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(
    k.faceTextSvg(
      k.topMatrix([0, strip.y + 5.8], zTop + 0.7, P, "x"),
      "WHEELBASE 192 MM · TRACK 125 MM · 1:14 4WD",
      { size: 2.8, tone: "mid", anchor: "middle" },
    ),
  );
  return out.join("");
}

// 01: 6061-T6 Aluminum Chassis Plate + Front Foam Bumper + Rear Diffuser
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

  // Side mudguards / rock sliders
  for (const side of [-1, 1]) {
    const guard = { x: -56, y: side > 0 ? 34 : -48, w: 112, d: 14, r: 3 };
    out.push(S(k.slabOf(guard, CHASSIS_Z + 1, 3.2, P, 4, 0.5), { tone: "lo" }));
    out.push(D([[-44, guard.y + 7, CHASSIS_Z + 4.2], [0, guard.y + 7, CHASSIS_Z + 4.2], [44, guard.y + 7, CHASSIS_Z + 4.2]].map(at), { size: 0.45 }));
  }

  // Front wide EVA foam rally bumper (-142 to -114)
  const bumper = { x: -142, y: -52, w: 24, d: 104, r: 9 };
  out.push(S(k.slabOf(bumper, CHASSIS_Z - 1, 8, P, 6, 1.0), { tone: "lo" }));
  out.push(L(k.planOutline(k.insetPlan(bumper, 3), CHASSIS_Z + 7, P, 4), { tone: "faint" }));
  // Front upper bumper brace & body posts
  const braceF = { x: -132, y: -32, w: 14, d: 64, r: 3 };
  out.push(S(k.slabOf(braceF, CHASSIS_Z + 7, 3, P, 4, 0.4), { tone: "mid" }));
  for (const py of [-22, 22]) {
    out.push(S(k.cylinder(-125, py, 2.4, CHASSIS_Z + 10, 22, P, 16), { tone: "mid" }));
    out.push(S(k.cylinder(-125, py, 3.4, CHASSIS_Z + 32, 2, P, 16), { tone: "hi" }));
  }

  // Rear diffuser bumper (+114 to +134)
  const bumperR = { x: 116, y: -44, w: 18, d: 88, r: 5 };
  out.push(S(k.slabOf(bumperR, CHASSIS_Z, 6, P, 5, 0.7), { tone: "lo" }));
  for (const dy of [-28, -14, 0, 14, 28]) {
    out.push(S(k.slabOf({ x: 120, y: dy - 1.2, w: 14, d: 2.4, r: 0.5 }, CHASSIS_Z - 1, 7.5, P, 2), { tone: "mid" }));
  }

  // Countersunk chassis screws & honeycomb stiffening ribs
  out.push(D(k.dotGrid(-36, -12, 4, 2, 16, zTop, P), { size: 0.42, tone: "lo" }));
  return out.join("");
}

// 02: LIT SUBJECT — Full-Time 4WD Metal Drivetrain (Center Shaft, Spur/Pinion, Front & Rear Metal Bevel Diffs, CVD Dogbones)
function buildDrivetrain() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;
  const shaftZ = zTop + 9;
  const F_X = G.frameOf([0, 0, shaftZ], [1, 0, 0], [0, 1, 0], [0, 0, 1]);

  // Front & Rear Metal Differential Housings + Internal Bevel Ring Gears
  for (const ax of [AXLE_F, AXLE_R]) {
    const housing = { x: ax - 13, y: -15, w: 26, d: 30, r: 4 };
    out.push(S(k.slabOf(housing, zTop, 18, P, 5, 0.8), { tone: "mid" }));
    out.push(L(k.planOutline(k.insetPlan(housing, 2.5), zTop + 18, P, 4), { tone: "lo" }));
    out.push(D(k.corners(housing, 3.5).map(([x, y]) => at([x, y, zTop + 18])), { size: 0.45 }));

    // Lit Metal Bevel Ring Gear visible inside cutaway window
    const F_Y = G.frameOf([ax, 0, shaftZ], [0, 1, 0], [1, 0, 0], [0, 0, 1]);
    out.push(S(G.disc(-5, 5, 8.2, F_Y, P, { bevel: 0.5 }), { tone: "hi", lit: true }));
    out.push(S(G.disc(-2.2, 2.2, 10.5, F_Y, P, { bevel: 0.6 }), { tone: "hi", lit: true }));

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
      out.push(S(G.disc(side > 0 ? 13 : -17, side > 0 ? 17 : -13, 3.6, F_Y, P), { tone: "hi", lit: true }));
    }
  }

  // Center Aluminum Main Driveshaft running from AXLE_F + 13 to AXLE_R - 13
  out.push(S(G.disc(AXLE_F + 13, AXLE_R - 13, 3.1, F_X, P, { bevel: 0.4 }), { tone: "hi", lit: true }));

  // 45T Metal Spur Gear + Slipper/Center Hub at x = 38
  out.push(S(G.disc(34, 40, 13.5, F_X, P, { bevel: 0.7 }), { tone: "hi", lit: true }));
  out.push(S(G.disc(32, 42, 6.2, F_X, P, { bevel: 0.4 }), { tone: "hi", lit: true }));

  // 15T Steel Pinion Gear meshing with 45T Spur Gear (offset at y = +15.5, z = shaftZ + 2)
  const F_PINION = G.frameOf([37, 15.5, shaftZ + 2], [1, 0, 0], [0, 1, 0], [0, 0, 1]);
  out.push(S(G.disc(-4, 4, 5.4, F_PINION, P, { bevel: 0.4 }), { tone: "hi", lit: true }));

  // Animated flow line along center drivetrain for visual torque flow
  out.push(
    L(k.segment([AXLE_F, 0, shaftZ + 11], [AXLE_R, 0, shaftZ + 11], P), {
      tone: "lit",
      dashed: true,
      flow: true,
      className: "mjx-torque-line",
      free: true,
    }),
  );
  return out.join("");
}

// 03: 2845 3700KV 4-Pole Brushless Motor + Finned Heatsink + Cooling Fan
function buildMotor() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;
  const motorZ = zTop + 11;
  const F_M = G.frameOf([8, 15.5, motorZ], [1, 0, 0], [0, 1, 0], [0, 0, 1]);

  // Motor mount bulkhead
  out.push(S(k.slabOf({ x: 25, y: 4, w: 6, d: 24, r: 1.5 }, zTop, 20, P, 3, 0.5), { tone: "mid" }));

  // 2845 Brushless Can (x = -16 to +25, radius = 10.5)
  out.push(S(G.disc(-16, 25, 10.5, F_M, P, { bevel: 0.8 }), { tone: "hi" }));

  // Aluminum Finned Heatsink Jacket (5 cooling rings around motor body)
  for (const s of [-10, -4, 2, 8, 14]) {
    out.push(S(G.disc(s - 1.2, s + 1.2, 12.2, F_M, P, { bevel: 0.3 }), { tone: "mid" }));
  }

  // Top 30x30 High-RPM Cooling Fan mounted above heatsink
  const fanPlan = { x: -10, y: 4.5, w: 22, d: 22, r: 2.5 };
  const fanZ = motorZ + 12.5;
  out.push(S(k.slabOf(fanPlan, fanZ, 5.5, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.ring(1, 15.5, 8.5, fanZ + 5.5, P, 28), { tone: "lo" }));
  out.push(S(k.cylinder(1, 15.5, 3.2, fanZ + 4, 1.8, P, 18), { tone: "hi" }));
  out.push(D(k.corners(fanPlan, 2.6).map(([x, y]) => at([x, y, fanZ + 5.5])), { size: 0.45 }));

  // 3-Phase Brushless Silicone Wires (U/V/W) from Motor to 45A ESC
  for (const [idx, dy] of [-3, 0, 3].entries()) {
    const route = [
      [-16, 15.5 + dy, motorZ + 3],
      [-24, 10 + dy * 1.4, motorZ + 10],
      [-24, -6 + dy * 1.4, motorZ + 10],
    ];
    for (const part of tubePieces(route, 1.25, P, { maxLength: 30 })) {
      out.push(tubeSvg(part, { tone: idx === 1 ? "hi" : "mid" }));
    }
  }
  return out.join("");
}

// 04: E45R 45A Brushless ESC & G3C Gyro Receiver Box
function buildEsc() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;

  // 45A ESC base + finned heatsink + capacitor bank
  const escPlan = { x: -42, y: -32, w: 28, d: 24, r: 2.5 };
  out.push(S(k.slabOf(escPlan, zTop, 11, P, 4, 0.6), { tone: "mid" }));
  for (let fx = escPlan.x + 3; fx < escPlan.x + escPlan.w - 3; fx += 4.2) {
    out.push(S(k.slabOf({ x: fx, y: escPlan.y + 3, w: 2.2, d: 18, r: 0.4 }, zTop + 11, 5, P, 2), { tone: "hi" }));
  }
  // Dual capacitor cylinders beside ESC
  out.push(S(k.cylinder(-11, -26, 3.2, zTop, 11, P, 18), { tone: "mid" }));
  out.push(S(k.cylinder(-11, -18, 3.2, zTop, 11, P, 18), { tone: "mid" }));

  // G3C Gyro 3-Channel Receiver Box behind ESC
  const rxPlan = { x: -64, y: -32, w: 18, d: 22, r: 2 };
  out.push(S(k.slabOf(rxPlan, zTop, 12, P, 4, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(rxPlan, 2), zTop + 12, P, 3), { tone: "lo" }));
  out.push(
    k.faceTextSvg(k.topMatrix([-55, -21], zTop + 12, P, "x"), "G3C GYRO", {
      size: 2.3,
      tone: "hi",
      anchor: "middle",
    }),
  );
  // 2.4GHz Vertical Antenna Tube
  out.push(S(k.cylinder(-60, -28, 1.1, zTop + 12, 34, P, 12), { tone: "hi" }));
  out.push(S(k.cylinder(-60, -28, 1.6, zTop + 46, 3, P, 12), { tone: "lo" }));
  return out.join("");
}

// 05: 7.4V 2S / 11.1V 3S Li-ion/LiPo Battery Pack & Hold-Down Strap
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
    k.faceTextSvg(k.topMatrix([31, -21], zTop + 18.5, P, "x"), "2S 7.4V · 2000mAh", {
      size: 2.7,
      tone: "hi",
      anchor: "middle",
    }),
  );

  // Upper hold-down strap bar & posts
  out.push(S(k.cylinder(31, -34, 2.0, zTop, 20.5, P, 14), { tone: "mid" }));
  out.push(S(k.cylinder(31, -8, 2.0, zTop, 20.5, P, 14), { tone: "mid" }));
  out.push(S(k.slabOf({ x: 26, y: -35, w: 10, d: 28, r: 1.5 }, zTop + 18.8, 2.2, P, 3, 0.4), { tone: "hi" }));
  return out.join("");
}

// 06: 17g Digital Steering Servo + Spring Servo Saver + Dual-Bellcrank Ackermann Rack
function buildServo() {
  const out = [];
  const zTop = CHASSIS_Z + CHASSIS_H;

  // 17g Digital Servo Body (front-right of chassis)
  const servoPlan = { x: -56, y: 10, w: 26, d: 14, r: 2 };
  out.push(S(k.slabOf(servoPlan, zTop, 16, P, 4, 0.6), { tone: "mid" }));
  out.push(S(k.cylinder(-50, 17, 4.2, zTop + 16, 2.5, P, 20), { tone: "hi" }));
  out.push(D([at([-50, 17, zTop + 18.5])], { size: 0.5, tone: "lo" }));

  // Dual-Bellcrank Steering Posts + Spring Servo Saver Column + Ackermann Tie-Rod Plate
  for (const py of [-11, 11]) {
    out.push(S(k.cylinder(-68, py, 3.8, zTop, 14, P, 20), { tone: "mid" }));
    out.push(S(k.cylinder(-68, py, 2.4, zTop + 14, 3, P, 16), { tone: "hi" }));
  }
  const dragLink = { x: -71, y: -13, w: 6, d: 26, r: 2 };
  out.push(S(k.slabOf(dragLink, zTop + 11, 2.8, P, 3, 0.4), { tone: "hi" }));

  // Tie rods out to front steering knuckles
  for (const side of [-1, 1]) {
    const route = [
      [-68, side * 11, zTop + 12],
      [AXLE_F + 5, side * (TRACK_Y - 12), WHEEL_Z - 2],
    ];
    for (const part of tubePieces(route, 1.3, P, { maxLength: 50 })) {
      out.push(tubeSvg(part, { tone: "mid" }));
    }
  }
  return out.join("");
}

// 07 & 08: Front & Rear Independent Double-Wishbone Suspension + CNC Shock Tower + Oil-Filled Coilovers
function buildSuspension(isFront) {
  const out = [];
  const ax = isFront ? AXLE_F : AXLE_R;
  const zTop = CHASSIS_Z + CHASSIS_H;

  // CNC Aluminum Shock Tower (Butterfly mount)
  const towerX = isFront ? ax + 6 : ax - 10;
  const tower = { x: towerX, y: -24, w: 4, d: 48, r: 1.5 };
  out.push(S(k.slabOf(tower, zTop + 14, 24, P, 4, 0.5), { tone: "mid" }));
  out.push(D([[-20, zTop + 35], [-14, zTop + 35], [14, zTop + 35], [20, zTop + 35]].map(([y, z]) => at([towerX + 2, y, z])), { size: 0.45 }));

  // Left & Right Lower A-Arms, Upper Camber Links, and Oil-Filled Coilover Shocks
  for (const side of [-1, 1]) {
    const yInner = side * 14;
    const yOuter = side * (TRACK_Y - 10);
    const armPlan = {
      x: ax - 9,
      y: side > 0 ? yInner : yOuter,
      w: 18,
      d: Math.abs(yOuter - yInner),
      r: 2.5,
    };
    out.push(S(k.slabOf(armPlan, zTop + 1, 3.2, P, 4, 0.4), { tone: "mid" }));

    const upperRoute = [
      [ax, side * 13, zTop + 15],
      [ax, side * (TRACK_Y - 11), WHEEL_Z + 7],
    ];
    for (const part of tubePieces(upperRoute, 1.4, P, { maxLength: 45 })) {
      out.push(tubeSvg(part, { tone: "mid" }));
    }

    const shockX = towerX + 2;
    const shockY = side * 22;
    const zBot = zTop + 5;
    const zSpringTop = zTop + 26;
    const zCapTop = zTop + 34;

    const springRings = Array.from({ length: 6 }, (_, i) =>
      k.ring(shockX, shockY, 3.8, zBot + 2 + ((zSpringTop - zBot - 4) * (i + 0.5)) / 6, P, 18),
    ).join("");
    out.push(S(k.cylinder(shockX, shockY, 1.6, zBot, zSpringTop - zBot, P, 14), { tone: "hi", crease: "none" }));
    out.push(L(springRings, { tone: "hi" }));
    out.push(S(k.cylinder(shockX, shockY, 3.6, zSpringTop - 7, zCapTop - (zSpringTop - 7), P, 20, 0.5), { tone: "hi" }));
    out.push(L(k.knurl(shockX, shockY, 3.8, zSpringTop - 2, zSpringTop, 18, P), { tone: "lo" }));
  }
  return out.join("");
}

// 09 & 10: Front & Rear 58mm Rally/Drift Wheels, 6-Spoke Rims, Brake Discs & Hubs
function buildWheels(isFront) {
  const out = [];
  const ax = isFront ? AXLE_F : AXLE_R;
  const sides = [-1, 1].sort((a, b) => depth(ax, a * TRACK_Y, WHEEL_Z) - depth(ax, b * TRACK_Y, WHEEL_Z));

  for (const side of sides) {
    const wy = side * TRACK_Y;
    const F_W = G.frameOf([ax, wy, WHEEL_Z], [0, side, 0], [1, 0, 0], [0, 0, 1]);
    const partAttr = isFront ? `data-wheel="front-${side > 0 ? "r" : "l"}"` : `data-wheel="rear-${side > 0 ? "r" : "l"}"`;

    const wheelGroup = [];
    wheelGroup.push(S(G.disc(-WHEEL_W / 2 - 4, -WHEEL_W / 2, 8.5, F_W, P), { tone: "mid" }));
    wheelGroup.push(
      S(G.disc(-WHEEL_W / 2, WHEEL_W / 2, WHEEL_R, F_W, P, { bevel: 1.4 }), {
        tone: "lo",
        inner: L(
          [-4, 0, 4].map((s) => G.arcOf(F_W, s, WHEEL_R, P)).join(""),
          { tone: "faint" },
        ),
      }),
    );
    wheelGroup.push(S(G.disc(WHEEL_W / 2 - 2.2, WHEEL_W / 2 + 0.4, WHEEL_R * 0.66, F_W, P, { bevel: 0.6 }), { tone: "hi" }));
    wheelGroup.push(S(G.disc(WHEEL_W / 2 + 0.4, WHEEL_W / 2 + 2.2, 3.8, F_W, P), { tone: "mid" }));
    wheelGroup.push(D(G.dotsOf(F_W, WHEEL_W / 2 + 0.5, WHEEL_R * 0.44, 6, P, { all: true }), { size: 0.5, tone: "lo" }));

    out.push(`<g ${partAttr}>${wheelGroup.join("")}</g>`);
  }
  return out.join("");
}

// Compute back-to-front painter's order + Audit Recorder registration
const R = A.recorder(P, {
  order: ORDER,
  spring: { stagger: 0.035, stiffness: 78, damping: 15, substeps: 4 },
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
  { id: "wheels_f", anchor: true, ref: [AXLE_F, 48, WHEEL_Z], box: [[-104, 52, 0], [-64, 70, 36]], svg: buildWheels(true) },
  { id: "wheels_r", anchor: true, ref: [AXLE_R, 48, WHEEL_Z], box: [[64, 52, 0], [104, 70, 36]], svg: buildWheels(false) },
];

for (const item of RAW_PARTS) {
  const shape = R.solid(A.box(item.box[0], item.box[1], { name: `${item.id}.hull`, anchor: Boolean(item.anchor) }));
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
    "美嘉欣 MJX Hyper Go 14303 (1/14 4WD 无刷拉力/漂移底盘) 等轴测机械解剖图：包含 6061-T6 铝合金底盘、中央金属主传动轴与前后金属差速器（焦点高亮）、2845 3700KV 四极无刷电机与散热风扇、45A 电调与 G3C 陀螺仪接收机、2S/3S 锂电池、17g 数字舵机阿克曼转向及四轮油压绞牙独立悬架。",
  body: svgBody,
});

const CSS = `
.mjx-wrap{max-width:960px;margin:0 auto}
.mjx-toolbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(195px,1fr));gap:10px;padding:12px 16px;border-top:1px solid var(--anatomy-faint);background:color-mix(in srgb,var(--anatomy-paper) 92%,var(--anatomy-lo) 8%)}
.mjx-ctrl{display:flex;flex-direction:column;gap:5px;font-size:12px;color:var(--anatomy-mid)}
.mjx-ctrl-head{display:flex;justify-content:space-between;align-items:center;font-weight:600;color:var(--anatomy-hi)}
.mjx-btn-row{display:flex;flex-wrap:wrap;gap:6px}
.mjx-btn{appearance:none;border:1px solid var(--anatomy-lo);background:var(--anatomy-paper);color:var(--anatomy-hi);padding:5px 10px;border-radius:4px;font-size:12px;font-family:inherit;cursor:pointer;transition:all .15s}
.mjx-btn:hover{border-color:var(--anatomy-hi)}
.mjx-btn[data-active]{background:var(--anatomy-lit);color:#111;border-color:var(--anatomy-lit);font-weight:600}
.mjx-slider{width:100%;accent-color:var(--anatomy-lit);cursor:pointer}
.mjx-telemetry{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:10px 16px;border-top:1px solid var(--anatomy-faint);font-variant-numeric:tabular-nums}
.mjx-stat{padding:6px 10px;border:1px solid var(--anatomy-faint);border-radius:4px}
.mjx-stat-label{font-size:10.5px;color:var(--anatomy-mid);text-transform:uppercase;letter-spacing:.04em}
.mjx-stat-val{font-size:15px;font-weight:700;color:var(--anatomy-hi);margin-top:2px}
.mjx-stat-val[data-lit]{color:var(--anatomy-lit)}
.mjx-parts-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(175px,1fr));gap:6px;margin-bottom:12px}
.mjx-part-btn{appearance:none;text-align:left;border:1px solid var(--anatomy-faint);background:transparent;color:var(--anatomy-mid);padding:6px 9px;border-radius:4px;font-size:11.5px;font-family:inherit;cursor:pointer;transition:all .15s;display:flex;align-items:center;gap:6px}
.mjx-part-btn:hover,.mjx-part-btn[data-on]{border-color:var(--anatomy-lit);color:var(--anatomy-hi);background:color-mix(in srgb,var(--anatomy-lit) 12%,transparent)}
.mjx-part-num{font-weight:700;color:var(--anatomy-lit);font-variant-numeric:tabular-nums}
.mjx-inspector{padding:12px 14px;border:1px solid var(--anatomy-lo);border-radius:6px;margin-bottom:12px;background:color-mix(in srgb,var(--anatomy-paper) 95%,var(--anatomy-lit) 5%)}
.mjx-inspector-title{font-size:14px;font-weight:700;color:var(--anatomy-hi);display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}
.mjx-inspector-spec{font-size:11.5px;color:var(--anatomy-lit);font-family:ui-monospace,monospace}
.mjx-inspector-desc{font-size:12.5px;line-height:1.55;color:var(--anatomy-mid);margin-top:6px}
.mjx-piece{transition:opacity .2s;cursor:pointer}
.iso-stage[data-focus] .mjx-piece:not([data-on]){opacity:0.24}
.iso-stage[data-focus] .mjx-piece[data-on]{opacity:1;filter:drop-shadow(0 0 6px color-mix(in srgb,var(--anatomy-lit) 45%,transparent))}
@media (max-width:680px){.mjx-telemetry{grid-template-columns:repeat(2,1fr)}}
`;

const partsButtonsHtml = ORDER.map(
  (id) =>
    `<button type="button" class="mjx-part-btn" data-part-btn="${id}"><span class="mjx-part-num">${PIECES[id].num}</span><span>${PIECES[id].name}</span></button>`,
).join("");

const customControlsHtml = `
<div class="mjx-toolbar">
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>视图与动作 (View & Action)</span><kbd>E / S</kbd></div>
    <div class="mjx-btn-row">
      <button type="button" class="mjx-btn" data-act="explode">爆炸拆解 (E)</button>
      <button type="button" class="mjx-btn" data-act="bump">避震下压 (S)</button>
      <button type="button" class="mjx-btn" data-act="gyro" data-active>G3C 陀螺仪开启</button>
    </div>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>电池电压 (Battery Pack)</span><span data-bat-label>2S · 7.4V</span></div>
    <div class="mjx-btn-row">
      <button type="button" class="mjx-btn" data-bat="2" data-active>2S 7.4V (标配 43km/h)</button>
      <button type="button" class="mjx-btn" data-bat="3">3S 11.1V (狂暴 62km/h)</button>
    </div>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>无刷油门 (Throttle)</span><span data-thr-val>35%</span></div>
    <input type="range" class="mjx-slider" data-thr min="0" max="100" value="35" aria-label="Throttle percentage"/>
  </div>
  <div class="mjx-ctrl">
    <div class="mjx-ctrl-head"><span>阿克曼转向 / 漂移角 (Steer)</span><span data-str-val>0°</span></div>
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
    <div class="mjx-stat-label">实时理论车速 (Ground Speed)</div>
    <div class="mjx-stat-val" data-lit data-tel-speed>15.0 km/h</div>
  </div>
  <div class="mjx-stat">
    <div class="mjx-stat-label">阿克曼内/外轮角 & 陀螺仪修正</div>
    <div class="mjx-stat-val" data-tel-steer>0.0° / 0.0° · Gyro 0°</div>
  </div>
</div>
`;

const inspectorHtml = `
<div class="mjx-inspector" data-inspector>
  <div class="mjx-inspector-title">
    <span data-ins-name>02 · 4WD 中央金属轴与前后伞齿差速器 (4WD Center Shaft & Metal Bevel Diffs)</span>
    <span class="mjx-inspector-spec" data-ins-spec>FDR 8.54:1 · 15T/45T 金属主齿 · 37T/13T 粉末冶金伞齿差速器</span>
  </div>
  <div class="mjx-inspector-desc" data-ins-desc>${PIECES.drivetrain.principle}</div>
</div>
<div class="mjx-parts-grid">${partsButtonsHtml}</div>
`;

const body = `<style>${CSS}</style><div class="mjx-wrap">${k.plateHtml({
  fig: "Fig 1 · MJX HYPER GO 14303",
  title: "美嘉欣 14303 · 1/14 全时四驱无刷拉力/漂移底盘机械原理",
  hint: "按 E 爆炸拆解 · 按 S 避震下压 · 点击总成查看机械原理",
  readout: "2S 7.4V · 15.0 km/h · Assembled",
  keys: [
    { mark: "lit", label: "核心动力链：15T/45T 主减速齿 → 中央铝合金轴 → 前后 37T/13T 金属伞齿差速器 → 四轮 CVD" },
    { mark: "raised", label: "10 大可拆解机械总成（支持点击/悬停独立高亮检视与物理联动）" },
  ],
  caption:
    inspectorHtml +
    "美嘉欣（MJX）Hyper Go 14303 采用 192 mm 轴距 6061-T6 铝合金主底盘与全车金属传动系统。2845 3700KV 四极无刷电机输出动力经初级齿轮副（45T/15T = 3.0）与前后粉末冶金伞齿差速器（37T/13T = 2.846，总减速比 8.54:1）分配至四轮；配备油压绞牙独立悬架与内置 G3C 陀螺仪的 17g 数字舵机阿克曼转向系统。",
  body: `<div class="iso-stage" tabindex="0" role="application" aria-label="美嘉欣 14303 底盘互动解剖台">${svg}</div>${customControlsHtml}`,
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
const btnExplode = document.querySelector('[data-act="explode"]');
const btnBump = document.querySelector('[data-act="bump"]');
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
const insName = document.querySelector("[data-ins-name]");
const insSpec = document.querySelector("[data-ins-spec]");
const insDesc = document.querySelector("[data-ins-desc]");
const torqueLine = svg.querySelector(".mjx-torque-line");
const frontLeftWheel = svg.querySelector('[data-wheel="front-l"]');
const frontRightWheel = svg.querySelector('[data-wheel="front-r"]');

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
let selected = null;
let clock = 0;
let last = 0;

const springs = Object.fromEntries(ORDER.map((id) => [id, { x: 0, v: 0, target: 0 }]));
const bumpState = { z: 0, v: 0 };

function selectPart(id) {
  selected = selected === id ? null : id;
  if (selected) {
    stage.setAttribute("data-focus", "");
    const info = PIECES[selected];
    insName.textContent = info.num + " · " + info.name + " (" + info.en + ")";
    insSpec.textContent = info.spec;
    insDesc.textContent = info.principle;
  } else {
    stage.removeAttribute("data-focus");
    const info = PIECES.drivetrain;
    insName.textContent = info.num + " · " + info.name + " (" + info.en + ")";
    insSpec.textContent = info.spec;
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

function triggerBump() {
  bumpState.v = -165;
  btnBump.setAttribute("data-active", "");
  setTimeout(() => btnBump.removeAttribute("data-active"), 380);
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
btnBump.addEventListener("click", () => triggerBump());
btnGyro.addEventListener("click", () => {
  gyroEnabled = !gyroEnabled;
  if (gyroEnabled) btnGyro.setAttribute("data-active", "");
  else btnGyro.removeAttribute("data-active");
  btnGyro.textContent = gyroEnabled ? "G3C 陀螺仪开启" : "G3C 陀螺仪关闭";
});

for (const b of batBtns) {
  b.addEventListener("click", () => {
    cells = Number(b.dataset.bat);
    for (const other of batBtns) {
      if (other === b) other.setAttribute("data-active", "");
      else other.removeAttribute("data-active");
    }
    batLabel.textContent = cells === 3 ? "3S · 11.1V" : "2S · 7.4V";
  });
}

thrInput.addEventListener("input", () => {
  throttle = Number(thrInput.value) / 100;
  thrVal.textContent = Math.round(throttle * 100) + "%";
});

strInput.addEventListener("input", () => {
  steerDeg = Number(strInput.value);
  strVal.textContent = (steerDeg > 0 ? "+" : "") + steerDeg + "°";
});

window.addEventListener("keydown", (e) => {
  if (e.key === "e" || e.key === "E") {
    e.preventDefault();
    toggleExplode();
  } else if (e.key === "s" || e.key === "S") {
    e.preventDefault();
    triggerBump();
  } else if (e.key === "ArrowLeft") {
    strInput.value = String(Math.max(-28, steerDeg - 4));
    strInput.dispatchEvent(new Event("input"));
  } else if (e.key === "ArrowRight") {
    strInput.value = String(Math.min(28, steerDeg + 4));
    strInput.dispatchEvent(new Event("input"));
  }
});

function tick(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 24) : 1 / 60;
  last = now;
  clock += dt;

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

  const gyroCounter = gyroEnabled && throttle > 0.25 ? Math.sin(clock * 4.5) * (throttle * 6.5) - steerDeg * 0.32 : 0;
  const netSteer = steerDeg + gyroCounter;
  const innerDeg = netSteer * 1.08;
  const outerDeg = netSteer * 0.84;

  for (const el of pieceEls) {
    const id = el.dataset.piece;
    const [mx, my, mz] = el.dataset.move.split(",").map(Number);
    const share = springs[id].x;
    let dz = mz * share;
    if (id === "chassis" || id === "drivetrain" || id === "motor" || id === "esc" || id === "battery" || id === "servo") {
      dz += bumpState.z * 0.55;
    } else if (id === "suspension_f" || id === "suspension_r") {
      dz += bumpState.z * 0.85;
    }
    el.setAttribute("transform", translateAlong(P, [mx * share, my * share, dz]));
  }

  if (frontLeftWheel && frontRightWheel) {
    const shiftL = (netSteer / 28) * 3.5;
    const shiftR = (netSteer / 28) * 3.5;
    frontLeftWheel.setAttribute("transform", translateAlong(P, [shiftL, shiftL * 0.6, 0]));
    frontRightWheel.setAttribute("transform", translateAlong(P, [-shiftR, shiftR * 0.6, 0]));
  }

  if (torqueLine) {
    torqueLine.style.animationDuration = throttle > 0.02 ? (0.95 - throttle * 0.78).toFixed(2) + "s" : "0s";
    torqueLine.style.opacity = throttle > 0.02 ? "1" : "0.25";
  }

  telMotor.textContent = motorRpm.toLocaleString("en-US") + " RPM";
  telWheel.textContent = wheelRpm.toLocaleString("en-US") + " RPM";
  telSpeed.textContent = speedKmh.toFixed(1) + " km/h";
  telSteer.textContent =
    innerDeg.toFixed(1) + "° / " + outerDeg.toFixed(1) + "° · Gyro " + (gyroCounter >= 0 ? "+" : "") + gyroCounter.toFixed(1) + "°";

  const stateLabel = apart ? "Exploded (10 Assemblies)" : Math.abs(bumpState.z) > 0.4 ? "Shock Travel " + bumpState.z.toFixed(1) + " mm" : "Assembled";
  const rText = cells + "S " + voltage.toFixed(1) + "V · " + speedKmh.toFixed(1) + " km/h · " + stateLabel;
  if (readout.textContent !== rText) readout.textContent = rText;

  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
`;

const outFile = join(HERE, theme === "light" ? "mjx-14303-chassis-light.html" : "mjx-14303-chassis.html");
writeFileSync(
  outFile,
  k.pageHtml({
    title: "MJX Hyper Go 14303 · 1/14 4WD RC 底盘机械解剖学",
    theme,
    body,
    script: kitScript() + live,
    width: 960,
  }),
);
console.log("wrote", outFile);

if (runAudit) {
  A.auditOrExit(R, P, { step: 1.0, clearanceStep: 1.0 });
}
