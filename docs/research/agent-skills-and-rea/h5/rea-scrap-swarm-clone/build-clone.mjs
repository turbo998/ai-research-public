import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>废土斗机祭 (Scrap Swarm) — morluto/rea 完整逆向复刻版 (实战 + 机甲整备库 + 剧情剧场 + AST 热补丁工作台)</title>
  <style>
    :root {
      --bg: #0f110e;
      --panel: #181b16;
      --panel-hi: #21261e;
      --border: #383e31;
      --accent: #f0b34f;
      --accent-hi: #ffe28a;
      --cyan: #00e5ff;
      --danger: #e25a3c;
      --emerald: #4ade80;
      --text: #ece7d5;
      --muted: #9ea392;
      --mono: "JetBrains Mono", "Cascadia Code", Consolas, monospace;
      --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: radial-gradient(circle at 20% 0%, #1c2119 0%, #0d0f0c 70%);
      color: var(--text);
      font-family: var(--sans);
      min-height: 100vh;
      padding: 14px 18px 28px;
    }
    .header-bar {
      max-width: 1440px;
      margin: 0 auto 12px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 18px;
      background: rgba(24, 27, 22, 0.92);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-badge {
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(240, 179, 79, 0.16);
      border: 1px solid var(--accent);
      color: var(--accent-hi);
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
    }
    .brand h1 {
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: #fff;
    }
    .brand p {
      font-size: 12px;
      color: var(--muted);
    }
    .nav-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .tab-btn {
      font-family: var(--sans);
      font-size: 12px;
      font-weight: 700;
      padding: 7px 13px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #141712;
      color: var(--muted);
      cursor: pointer;
      transition: all 0.15s;
    }
    .tab-btn:hover {
      border-color: var(--accent);
      color: var(--text);
    }
    .tab-btn.active {
      background: rgba(240, 179, 79, 0.18);
      border-color: var(--accent);
      color: var(--accent-hi);
      box-shadow: 0 0 14px rgba(240, 179, 79, 0.22);
    }
    .portal-link {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--cyan);
      text-decoration: none;
      padding: 6px 10px;
      border: 1px solid rgba(0, 229, 255, 0.35);
      border-radius: 7px;
      background: rgba(0, 229, 255, 0.08);
    }
    .portal-link:hover {
      background: rgba(0, 229, 255, 0.18);
    }

    /* Main Workspace Layout */
    .workspace {
      max-width: 1440px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr 430px;
      gap: 14px;
      align-items: start;
    }
    @media (max-width: 1150px) {
      .workspace { grid-template-columns: 1fr; }
    }

    /* Left Primary Stage */
    .stage-card {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
    }
    .view-pane { display: none; }
    .view-pane.active { display: block; }

    /* Arena HUD */
    .hud-top {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 8px;
      padding: 10px 14px;
      background: #131611;
      border-bottom: 1px solid var(--border);
    }
    .hud-stat {
      background: var(--panel-hi);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 7px;
      padding: 6px 9px;
    }
    .hud-stat-label {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--muted);
      text-transform: uppercase;
    }
    .hud-stat-val {
      font-family: var(--mono);
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-hi);
      margin-top: 2px;
    }
    .arena-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 10;
      background: #141712;
      overflow: hidden;
    }
    #gameCanvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }

    /* Tactical Cut-in Banner inside Arena */
    .cutin-banner {
      position: absolute;
      left: 18px;
      right: 18px;
      top: 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 16px;
      border-radius: 10px;
      background: linear-gradient(90deg, rgba(16, 20, 15, 0.95) 0%, rgba(36, 32, 22, 0.92) 70%, rgba(16, 20, 15, 0.85) 100%);
      border: 1.5px solid var(--accent);
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.65);
      transform: translateY(-130%);
      opacity: 0;
      transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1);
      pointer-events: none;
      z-index: 20;
    }
    .cutin-banner.show {
      transform: translateY(0);
      opacity: 1;
    }
    .cutin-avatar {
      width: 54px;
      height: 54px;
      flex-shrink: 0;
      border-radius: 8px;
      background: #121510;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .cutin-avatar svg { width: 46px; height: 46px; }
    .cutin-meta { flex: 1; }
    .cutin-speaker {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--accent);
    }
    .cutin-title {
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      margin: 1px 0 2px;
    }
    .cutin-sub {
      font-size: 12px;
      color: var(--text);
    }

    /* Story Modal Overlay inside Arena */
    .story-overlay {
      position: absolute;
      inset: 0;
      background: rgba(10, 12, 9, 0.86);
      backdrop-filter: blur(4px);
      display: none;
      flex-direction: column;
      justify-content: flex-end;
      padding: 22px;
      z-index: 30;
    }
    .story-overlay.active { display: flex; }
    .story-card {
      background: linear-gradient(180deg, #1b2018 0%, #121510 100%);
      border: 1.5px solid var(--accent);
      border-radius: 12px;
      padding: 18px 20px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.75);
    }
    .story-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }
    .story-act {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--accent);
      font-weight: 700;
    }
    .story-loc {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
    }
    .story-body {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      margin: 10px 0 14px;
    }
    .story-portrait {
      width: 68px;
      height: 68px;
      border-radius: 10px;
      background: #10130e;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .story-portrait svg { width: 58px; height: 58px; }
    .story-speaker-name {
      font-size: 13px;
      font-weight: 800;
      color: var(--accent-hi);
    }
    .story-speaker-role {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      margin-left: 8px;
    }
    .story-text {
      font-size: 14px;
      line-height: 1.65;
      color: var(--text);
      margin-top: 6px;
    }
    .story-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .story-step-indicator {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
    }

    /* Controls Bar below Arena */
    .arena-controls {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 10px 14px;
      background: #131611;
      border-top: 1px solid var(--border);
    }
    .btn-group { display: flex; flex-wrap: wrap; gap: 6px; }
    .act-btn {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      padding: 6px 11px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--panel-hi);
      color: var(--text);
      cursor: pointer;
      transition: all 0.14s;
    }
    .act-btn:hover {
      border-color: var(--accent);
      color: var(--accent-hi);
    }
    .act-btn.primary {
      background: rgba(240, 179, 79, 0.2);
      border-color: var(--accent);
      color: var(--accent-hi);
    }

    /* Hangar Tab */
    .hangar-layout {
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .hangar-top-controls {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 10px;
    }
    .hangar-stage-grid {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 14px;
    }
    @media (max-width: 820px) {
      .hangar-stage-grid { grid-template-columns: 1fr; }
    }
    .hangar-canvas-box {
      background: #121510;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      position: relative;
    }
    #hangarCanvas {
      width: 100%;
      height: 390px;
      display: block;
    }
    .hangar-spec-box {
      background: #131611;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .hangar-unit-title {
      font-size: 18px;
      font-weight: 800;
      color: var(--accent-hi);
    }
    .hangar-unit-role {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--cyan);
    }
    .hangar-stats-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
    }
    .hangar-stat-pill {
      background: var(--panel-hi);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 8px;
      font-family: var(--mono);
      font-size: 11px;
    }
    .hangar-stat-pill span {
      display: block;
      font-size: 9px;
      color: var(--muted);
    }
    .hangar-callout-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 4px;
    }
    .hangar-callout-item {
      background: rgba(255,255,255,0.03);
      border-left: 3px solid var(--accent);
      padding: 6px 10px;
      border-radius: 0 6px 6px 0;
      font-size: 12px;
    }
    .hangar-callout-item strong {
      color: var(--accent-hi);
      font-family: var(--mono);
      margin-right: 6px;
    }

    /* Story Theater Tab */
    .theater-layout {
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .chapter-Lines {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .dialogue-row {
      display: flex;
      gap: 12px;
      padding: 12px;
      background: #131611;
      border: 1px solid var(--border);
      border-radius: 10px;
      align-items: flex-start;
    }
    .dialogue-row.highlight {
      border-color: var(--accent);
      background: rgba(240, 179, 79, 0.07);
    }

    /* Right Sidebar: REA Reverse Engineering & Hot-Patch Inspector */
    .inspector-card {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
    }
    .inspector-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }
    .inspector-head h2 {
      font-size: 14px;
      font-weight: 800;
      color: var(--cyan);
      font-family: var(--mono);
    }
    .sec-title {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }
    .code-compare {
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
    }
    .code-box {
      background: #0c0e0b;
      border: 1px solid #2b3126;
      border-radius: 8px;
      padding: 9px 11px;
      font-family: var(--mono);
      font-size: 11px;
      line-height: 1.45;
      color: #c5d1b8;
      overflow-x: auto;
      max-height: 175px;
      white-space: pre;
    }
    .code-box-tag {
      display: flex;
      justify-content: space-between;
      font-family: var(--mono);
      font-size: 10px;
      color: var(--muted);
      margin-bottom: 4px;
    }
    .patch-grid {
      display: flex;
      flex-direction: column;
      gap: 8px;
      background: #131611;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
    }
    .patch-row {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .patch-row-head {
      display: flex;
      justify-content: space-between;
      font-family: var(--mono);
      font-size: 11px;
    }
    .patch-row input[type=range] {
      width: 100%;
      accent-color: var(--cyan);
      cursor: pointer;
    }
    .soundboard-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
    }
    .sfx-btn {
      font-family: var(--mono);
      font-size: 10px;
      padding: 5px 6px;
      border-radius: 5px;
      border: 1px solid var(--border);
      background: #131611;
      color: var(--text);
      cursor: pointer;
      text-align: left;
    }
    .sfx-btn:hover {
      border-color: var(--cyan);
      color: var(--cyan);
    }
    .ev-ledger-list {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .ev-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 5px 8px;
      border-radius: 6px;
      background: #11140f;
      border: 1px solid #2b3126;
      font-family: var(--mono);
      font-size: 10px;
      transition: all 0.2s;
    }
    .ev-item.pulse {
      border-color: var(--emerald);
      background: rgba(74, 222, 128, 0.14);
      box-shadow: 0 0 10px rgba(74, 222, 128, 0.25);
    }
    .ev-hash {
      color: var(--cyan);
      font-weight: 700;
    }
    .ev-desc {
      color: var(--text);
    }
    .ev-meta {
      color: var(--muted);
      font-size: 9.5px;
    }
  </style>
</head>
<body>
  <header class="header-bar">
    <div class="brand">
      <span class="brand-badge">REA REVERSE-ENGINEERED CLONE · V2 FULL ARCHIVE</span>
      <div>
        <h1>《废土斗机祭 Scrap Swarm》— 完整逆向复刻与 AST 热补丁实验台</h1>
        <p>基于 morluto/rea 从 Vite 混淆产物 (index-Da3qZ_pX.js) 1:1 还原：五机甲多关节运动学 + 整备库 + 五章剧情剧场 + Web Audio 双振荡合成器</p>
      </div>
    </div>
    <div class="nav-tabs">
      <button type="button" class="tab-btn active" data-tab="arena">⚔️ 废土实战剧场 (Arena)</button>
      <button type="button" class="tab-btn" data-tab="hangar">🛠️ 五机甲整备库 (5 Units × 4 Poses)</button>
      <button type="button" class="tab-btn" data-tab="story">📜 五章战役剧情与特写 (Story & Cut-Ins)</button>
    </div>
    <a class="portal-link" href="../../index.html">← 返回研究总门户</a>
  </header>

  <main class="workspace">
    <!-- Left Primary Stage -->
    <section class="stage-card">
      <!-- TAB 1: ARENA -->
      <div class="view-pane active" id="pane-arena">
        <div class="hud-top">
          <div class="hud-stat">
            <div class="hud-stat-label">机体装甲 (HP / 护盾)</div>
            <div class="hud-stat-val" id="hudHp">120 / 45</div>
          </div>
          <div class="hud-stat">
            <div class="hud-stat-label">战役幕次 (Act)</div>
            <div class="hud-stat-val" id="hudAct">ACT I · 残铁点火</div>
          </div>
          <div class="hud-stat">
            <div class="hud-stat-label">当前主武器 (Weapon)</div>
            <div class="hud-stat-val" id="hudWeapon">铆钉机炮 [1]</div>
          </div>
          <div class="hud-stat">
            <div class="hud-stat-label">蒸汽超载 (Overdrive)</div>
            <div class="hud-stat-val" id="hudOverdrive">READY [Q]</div>
          </div>
          <div class="hud-stat">
            <div class="hud-stat-label">废铁结晶 (Scrap)</div>
            <div class="hud-stat-val" id="hudScrap">0</div>
          </div>
          <div class="hud-stat">
            <div class="hud-stat-label">铁冠领主 (Boss Lock)</div>
            <div class="hud-stat-val" id="hudBoss">未降临</div>
          </div>
        </div>

        <div class="arena-wrap">
          <canvas id="gameCanvas" width="960" height="600"></canvas>

          <!-- Tactical Cut-in Banner -->
          <div class="cutin-banner" id="cutinBanner">
            <div class="cutin-avatar" id="cutinAvatar"></div>
            <div class="cutin-meta">
              <div class="cutin-speaker" id="cutinSpeaker">R-17 铁骑 · 凯尔 (KAEL)</div>
              <div class="cutin-title" id="cutinTitle">“蒸汽超载阀全开——撕碎敌阵！”</div>
              <div class="cutin-sub" id="cutinSub">OVERDRIVE CORE ENGAGED · 攻速翻倍 · 散热翼展开</div>
            </div>
          </div>

          <!-- Story Modal Overlay inside Arena -->
          <div class="story-overlay" id="storyOverlay">
            <div class="story-card">
              <div class="story-head">
                <span class="story-act" id="modalStoryAct">PROLOGUE // 00 · 序幕：残铁点火</span>
                <span class="story-loc" id="modalStoryLoc">锈锚盆地 · 7号整备窖</span>
              </div>
              <div class="story-body">
                <div class="story-portrait" id="modalStoryPortrait"></div>
                <div style="flex:1">
                  <div>
                    <span class="story-speaker-name" id="modalStorySpeaker">林顿·薇拉 (Vela)</span>
                    <span class="story-speaker-role" id="modalStoryRole">首席整备师 · 灰烬信标</span>
                  </div>
                  <div class="story-text" id="modalStoryText"></div>
                </div>
              </div>
              <div class="story-footer">
                <span class="story-step-indicator" id="modalStoryStep">LINE 1 / 3</span>
                <div class="btn-group">
                  <button type="button" class="act-btn" id="btnSkipStory">跳过本章 (Skip)</button>
                  <button type="button" class="act-btn primary" id="btnNextStory">下一句 (Space / Click) →</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="arena-controls">
          <div class="btn-group">
            <button type="button" class="act-btn primary" id="btnAutoPlay">🤖 AI 自动巡航演示: ON</button>
            <button type="button" class="act-btn" id="btnSwitchWeapon">切换三武器 (1/2/3)</button>
            <button type="button" class="act-btn" id="btnDash">💨 推进冲刺 (Space)</button>
            <button type="button" class="act-btn" id="btnTriggerOverdrive">⚡ 释放蒸汽超载 (Q)</button>
            <button type="button" class="act-btn" id="btnShelterEmp">🌐 避难所磁暴脉冲 (E)</button>
            <button type="button" class="act-btn" id="btnSpawnBoss">👑 立即召唤铁冠领主 Boss</button>
            <button type="button" class="act-btn" id="btnTriggerCutin">🎬 触发特写横幅</button>
            <button type="button" class="act-btn" id="btnOpenPrologue">📖 播放战役剧情弹窗</button>
          </div>
          <div style="font-family:var(--mono);font-size:11px;color:var(--muted)">
            WASD 移动 · 鼠标瞄准 · 1/2/3 切武器 · Space 冲刺 · Q 超载
          </div>
        </div>
      </div>

      <!-- TAB 2: MECHA HANGAR (5 UNITS x 4 POSES) -->
      <div class="view-pane" id="pane-hangar">
        <div class="hangar-layout">
          <div class="hangar-top-controls">
            <div class="btn-group" id="hangarUnitBtns"></div>
            <div class="btn-group" id="hangarPoseBtns"></div>
            <button type="button" class="act-btn" id="btnHangarXray">🔍 内部骨架透视 (X-Ray)</button>
          </div>
          <div class="hangar-stage-grid">
            <div class="hangar-canvas-box">
              <canvas id="hangarCanvas" width="580" height="400"></canvas>
            </div>
            <div class="hangar-spec-box">
              <div>
                <div class="hangar-unit-role" id="hangarRole">主角驾驶机体 · 重型拾荒突击铁骑</div>
                <div class="hangar-unit-title" id="hangarName">R-17 拾荒铁骑 · 铆钉号</div>
              </div>
              <div class="hangar-stats-grid">
                <div class="hangar-stat-pill"><span>装甲结构</span><strong id="hangarArmor">铆接复合钢 + 磁盾</strong></div>
                <div class="hangar-stat-pill"><span>主动力源</span><strong id="hangarReactor">双回路高压蒸汽核</strong></div>
                <div class="hangar-stat-pill"><span>主武装</span><strong id="hangarWeapon">铆钉机炮 / 电弧 / 震锤</strong></div>
              </div>
              <p id="hangarLore" style="font-size:12.5px;line-height:1.6;color:var(--text);background:#0f120d;padding:10px;border-radius:8px;border:1px solid var(--border)"></p>
              <div class="sec-title" style="margin-top:4px">🔩 REA 逆向还原多关节部件引线 (Callouts)</div>
              <div class="hangar-callout-list" id="hangarCallouts"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: STORY & CUT-IN THEATER -->
      <div class="view-pane" id="pane-story">
        <div class="theater-layout">
          <div class="hangar-top-controls">
            <div class="btn-group" id="storyChapterBtns"></div>
            <button type="button" class="act-btn primary" id="btnPlayChapterInArena">▶ 在实战剧场中全屏演示本章</button>
          </div>
          <div id="storyChapterHeader" style="padding:12px 14px;background:#131611;border:1px solid var(--border);border-radius:10px"></div>
          <div class="chapter-Lines" id="storyLinesContainer"></div>
          <div class="sec-title" style="margin-top:6px">⚡ 四大战术特写横幅 (CUTIN_SPECS) 一键预览</div>
          <div class="btn-group" id="cutinPreviewBtns"></div>
        </div>
      </div>
    </section>

    <!-- Right Sidebar: REA Decompiler & Live Memory Hot-Patch Workbench -->
    <aside class="inspector-card">
      <div class="inspector-head">
        <h2>🔬 REA AST & 内存热补丁工作台</h2>
        <span style="font-family:var(--mono);font-size:10px;color:var(--emerald)">● LIVE HOOK ATTACHED</span>
      </div>

      <div>
        <div class="sec-title">1. Bundle 混淆切片 ↔ 还原 AST 模块对照</div>
        <div class="btn-group" id="astModuleBtns" style="margin-bottom:8px">
          <button type="button" class="act-btn primary" data-ast="hangar">hangar.ts</button>
          <button type="button" class="act-btn" data-ast="data">data.ts</button>
          <button type="button" class="act-btn" data-ast="story">story.ts</button>
          <button type="button" class="act-btn" data-ast="audio">audio.ts</button>
          <button type="button" class="act-btn" data-ast="prng">prng.ts</button>
          <button type="button" class="act-btn" data-ast="physics">physics.ts</button>
          <button type="button" class="act-btn" data-ast="director">director.ts</button>
          <button type="button" class="act-btn" data-ast="spatial">spatial.ts</button>
          <button type="button" class="act-btn" data-ast="combat">combat.ts</button>
          <button type="button" class="act-btn" data-ast="save">save.ts</button>
          <button type="button" class="act-btn" data-ast="hud">hud.ts</button>
        </div>
        <div class="code-compare">
          <div>
            <div class="code-box-tag"><span>📦 生产构建混淆切片 (dist/assets/index-Da3qZ_pX.js)</span><span>Minified ES2022</span></div>
            <div class="code-box" id="minifiedCodeBox"></div>
          </div>
          <div>
            <div class="code-box-tag"><span>✨ REA 语义等价重构源码 (Reconstructed TypeScript)</span><span>100% Parity</span></div>
            <div class="code-box" id="decompiledCodeBox" style="color:#9cd7c8"></div>
          </div>
        </div>
      </div>

      <div>
        <div class="sec-title">2. 运行时常量热补丁注入 (Live Memory Hot-Patch)</div>
        <div class="patch-grid">
          <div class="patch-row">
            <div class="patch-row-head"><span>player.moveSpeed (机甲巡航移速)</span><strong id="valSpeed">245 px/s</strong></div>
            <input type="range" id="patchSpeed" min="140" max="460" step="5" value="245" />
          </div>
          <div class="patch-row">
            <div class="patch-row-head"><span>weapon.fireRateScale (主武器射速倍率)</span><strong id="valFireRate">1.00×</strong></div>
            <input type="range" id="patchFireRate" min="0.5" max="3.0" step="0.1" value="1.0" />
          </div>
          <div class="patch-row">
            <div class="patch-row-head"><span>boss.chestLockExposeSec (铁冠破盾暴露窗口)</span><strong id="valBossExpose">4.5 s</strong></div>
            <input type="range" id="patchBossExpose" min="2.0" max="10.0" step="0.5" value="4.5" />
          </div>
          <div class="patch-row">
            <div class="patch-row-head"><span>player.magnetRadius (废铁磁吸牵引半径)</span><strong id="valMagnet">175 px</strong></div>
            <input type="range" id="patchMagnet" min="80" max="360" step="10" value="175" />
          </div>
          <div class="patch-row">
            <div class="patch-row-head"><span>weapon.arcChainCount (电弧枪连锁跳数)</span><strong id="valArcChain">3 跳</strong></div>
            <input type="range" id="patchArcChain" min="2" max="7" step="1" value="3" />
          </div>
          <div class="patch-row">
            <div class="patch-row-head"><span>player.overdriveDuration (蒸汽超载持续时间)</span><strong id="valOverdriveDur">6.0 s</strong></div>
            <input type="range" id="patchOverdriveDur" min="3.0" max="15.0" step="0.5" value="6.0" />
          </div>
        </div>
      </div>

      <div>
        <div class="sec-title">3. Web Audio 双振荡合成器测试台 (ProceduralAudioEngine)</div>
        <div class="soundboard-grid" id="soundboardGrid"></div>
      </div>

      <div>
        <div class="sec-title">4. REA 密码学证据链实时脉动台账 (ev_&lt;sha256&gt;)</div>
        <div class="ev-ledger-list" id="evLedgerList">
          <div class="ev-item" data-ev="hangar"><span class="ev-hash">ev_7d31e804</span><span class="ev-desc">drawHangarR17..Boss (5机甲运动学)</span><span class="ev-meta">AST:1,420</span></div>
          <div class="ev-item" data-ev="weapon"><span class="ev-hash">ev_a9f4c218</span><span class="ev-desc">WEAPON_SPECS (铆钉/铁锤/电弧)</span><span class="ev-meta">AST:680</span></div>
          <div class="ev-item" data-ev="boss"><span class="ev-hash">ev_c4829b11</span><span class="ev-desc">IronCrown.chestLock (破盾2.5×)</span><span class="ev-meta">AST:910</span></div>
          <div class="ev-item" data-ev="emp"><span class="ev-hash">ev_39a7d42e</span><span class="ev-desc">ShelterBeacon.pulseEMP (磁暴)</span><span class="ev-meta">AST:540</span></div>
          <div class="ev-item" data-ev="story"><span class="ev-hash">ev_e8201f7c</span><span class="ev-desc">STORY_CHAPTERS & CUTIN_SPECS</span><span class="ev-meta">AST:1,150</span></div>
          <div class="ev-item" data-ev="audio"><span class="ev-hash">ev_51b0e93a</span><span class="ev-desc">ProceduralAudioEngine.tone()</span><span class="ev-meta">AST:490</span></div>
        </div>
      </div>
    </aside>
  </main>

  <script>
    // =========================================================================
    // 1. PROCEDURAL WEB AUDIO SYNTHESIZER (Reconstructed from src/game/audio.ts)
    // =========================================================================
    class ProceduralAudioEngine {
      constructor() {
        this.ctx = null;
        this.muted = false;
      }
      ensure() {
        if (this.muted) return null;
        if (!this.ctx) {
          const Ctor = window.AudioContext || window.webkitAudioContext;
          if (Ctor) this.ctx = new Ctor();
        }
        if (this.ctx && this.ctx.state === "suspended") {
          this.ctx.resume().catch(() => {});
        }
        return this.ctx;
      }
      tone(f0, f1, dur, type = "sawtooth", gain = 0.05, delay = 0) {
        const ctx = this.ensure();
        if (!ctx) return;
        const t0 = ctx.currentTime + delay;
        const osc = ctx.createOscillator();
        const g = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(Math.max(24, f0), t0);
        osc.frequency.exponentialRampToValueAtTime(Math.max(24, f1), t0 + dur);
        g.gain.setValueAtTime(gain, t0);
        g.gain.exponentialRampToValueAtTime(0.0008, t0 + dur);
        osc.connect(g);
        g.connect(ctx.destination);
        osc.start(t0);
        osc.stop(t0 + dur);
      }
      play(kind) {
        switch (kind) {
          case "shot":
            this.tone(420, 130, 0.07, "sawtooth", 0.045);
            this.tone(920, 280, 0.04, "square", 0.025);
            break;
          case "pulse":
            this.tone(150, 48, 0.2, "triangle", 0.075);
            this.tone(240, 62, 0.16, "sawtooth", 0.05);
            break;
          case "arc":
            this.tone(980, 420, 0.09, "square", 0.04);
            this.tone(640, 1280, 0.08, "sawtooth", 0.03, 0.03);
            break;
          case "dash":
            this.tone(180, 520, 0.11, "triangle", 0.05);
            break;
          case "hit":
            this.tone(280, 95, 0.05, "square", 0.03);
            break;
          case "hurt":
            this.tone(130, 52, 0.16, "sawtooth", 0.065);
            break;
          case "kill":
            this.tone(320, 620, 0.09, "triangle", 0.045);
            break;
          case "shelterPulse":
            this.tone(260, 520, 0.22, "sine", 0.06);
            this.tone(520, 780, 0.18, "triangle", 0.04, 0.06);
            break;
          case "lockExpose":
            this.tone(540, 220, 0.14, "sawtooth", 0.055);
            this.tone(720, 1080, 0.18, "triangle", 0.05, 0.1);
            break;
          case "cutin":
            this.tone(330, 660, 0.12, "triangle", 0.055);
            this.tone(440, 880, 0.16, "sawtooth", 0.045, 0.08);
            break;
          case "winFanfare":
            this.tone(392, 523.25, 0.18, "triangle", 0.06, 0);
            this.tone(523.25, 659.25, 0.18, "triangle", 0.06, 0.16);
            this.tone(659.25, 783.99, 0.32, "sawtooth", 0.065, 0.32);
            break;
        }
      }
    }
    const audio = new ProceduralAudioEngine();

    // =========================================================================
    // 2. SPEAKER PORTRAIT SVG & STORY CHAPTERS (Reconstructed from story.ts)
    // =========================================================================
    function speakerBadgeSvg(speaker) {
      if (speaker === "kael") {
        return \`<svg viewBox="0 0 64 64"><rect x="6" y="6" width="52" height="52" rx="10" fill="#232920" stroke="#c3a060" stroke-width="2.5"/><rect x="14" y="16" width="36" height="28" rx="6" fill="#595f50" stroke="#181b16" stroke-width="2"/><rect x="18" y="23" width="28" height="10" rx="2" fill="#141e17"/><rect x="21" y="26" width="22" height="4" fill="#b9dd78"/><path d="M18 48 L46 48 L40 56 L24 56 Z" fill="#b7863d"/></svg>\`;
      }
      if (speaker === "vela") {
        return \`<svg viewBox="0 0 64 64"><rect x="6" y="6" width="52" height="52" rx="10" fill="#1e2624" stroke="#7fc7b8" stroke-width="2.5"/><circle cx="32" cy="28" r="14" fill="#465853" stroke="#161d1b" stroke-width="2"/><circle cx="27" cy="27" r="4" fill="#00e5ff"/><circle cx="38" cy="27" r="3" fill="#ffe28a"/><path d="M18 48 Q32 40 46 48" stroke="#7fc7b8" stroke-width="3" fill="none"/></svg>\`;
      }
      return \`<svg viewBox="0 0 64 64"><rect x="6" y="6" width="52" height="52" rx="10" fill="#2a1d19" stroke="#e25a3c" stroke-width="2.5"/><polygon points="16,24 26,14 32,22 38,14 48,24 44,44 20,44" fill="#63372c" stroke="#1b1210" stroke-width="2"/><rect x="22" y="28" width="20" height="5" fill="#ffb548"/><circle cx="32" cy="40" r="5" fill="#e25a3c"/></svg>\`;
    }

    const CUTIN_SPECS = {
      overdrive: {
        speaker: "kael",
        speakerTag: "R-17 铁骑 · 凯尔 (KAEL)",
        title: "“蒸汽超载阀全开——撕碎敌阵！”",
        subtitle: "OVERDRIVE CORE ENGAGED · 攻速翻倍 · 散热翼展开",
      },
      shelter: {
        speaker: "vela",
        speakerTag: "整备台 · 林顿·薇拉 (VELA)",
        title: "“避难所磁暴脉冲释放——护盾回路满载！”",
        subtitle: "SHELTER EMP ACTIVATED · 全屏震退 + 装甲修复",
      },
      boss_entry: {
        speaker: "warden",
        speakerTag: "铁冠领主 · 典狱官 (WARDEN)",
        title: "“低等拾荒机，跪倒在铁冠反应炉前吧！”",
        subtitle: "BOSS WARNING · 击碎周围敌群以迫使胸口核心锁暴露",
      },
      boss_lock_open: {
        speaker: "vela",
        speakerTag: "整备台 · 林顿·薇拉 (VELA)",
        title: "“铁冠胸口核心锁已弹开！集火蓝色弱点！”",
        subtitle: "LOCK EXPOSED · 2.5× 弱点暴击倍率窗口开启",
      },
    };

    const STORY_CHAPTERS = [
      {
        id: "prologue",
        actLabel: "PROLOGUE // 00",
        title: "序幕：残铁点火",
        location: "锈锚盆地 · 7号整备窖",
        lines: [
          {
            speaker: "vela",
            name: "林顿·薇拉 (Vela)",
            role: "首席整备师 · 灰烬信标",
            text: "凯尔，听得见吗？R-17「铆钉号」的二号蒸汽锅炉刚完成冷铆合，磁轨护盾发生器只有 65% 的额定出力，别在第一波锯蟹潮里把液压臂震裂了。",
          },
          {
            speaker: "kael",
            name: "凯尔 (Kael)",
            role: "R-17 拾荒铁骑驾驶员",
            text: "只要右手这门 32mm 铆钉机炮还能退壳，就没人能跨过避难所防线。把反应炉压力表推到红区吧，薇拉。",
          },
          {
            speaker: "vela",
            name: "林顿·薇拉 (Vela)",
            role: "首席整备师 · 灰烬信标",
            text: "记住战术规程：[1] 铆钉机炮点射破甲、[2] 震荡铁锤近身清场、[3] 串联电弧枪连锁麻痹。收集废铁结晶随时回避难所充能！",
          },
        ],
      },
      {
        id: "act1_after",
        actLabel: "ACT I // CLEAR",
        title: "第一幕后：锯轮残响",
        location: "外环废铁河床 · 前哨残骸",
        lines: [
          {
            speaker: "kael",
            name: "凯尔 (Kael)",
            role: "R-17 拾荒铁骑驾驶员",
            text: "前锋掘进锯蟹群已经被清理干净了，但地面的低频震动还没停……重型铁砧机正在往盆地中央合围。",
          },
          {
            speaker: "vela",
            name: "林顿·薇拉 (Vela)",
            role: "首席整备师 · 灰烬信标",
            text: "雷达回波显示第二梯队混编了浮游电弧台（Zapper）。我刚把你的蒸汽超载阀（[Q] 键）解锁了，开启后双肩散热翼会强制排热，机炮射速翻倍！",
          },
        ],
      },
      {
        id: "act2_event",
        actLabel: "ACT II // MID",
        title: "第二幕中：风暴压境",
        location: "高压电弧雷区 · 信号盲段",
        lines: [
          {
            speaker: "warden",
            name: "铁冠典狱官 (Warden)",
            role: "废土中枢 · 铁冠重工统合体",
            text: "警告编号 R-17 的非法拼装机：立即停止采集核心废铁，向铁冠重工移交反应炉控制权，否则将执行熔毁处决。",
          },
          {
            speaker: "kael",
            name: "凯尔 (Kael)",
            role: "R-17 拾荒铁骑驾驶员",
            text: "废话真多。你们丢在废土上的每一颗铆钉，现在都姓灰烬信标了！",
          },
        ],
      },
      {
        id: "act3_eve",
        actLabel: "ACT III // BOSS",
        title: "第三幕前：铁冠降临",
        location: "熔渣核心祭坛 · 决战圈",
        lines: [
          {
            speaker: "warden",
            name: "铁冠典狱官 (Warden)",
            role: "铁冠领主 · 巨型攻城重机",
            text: "铁冠胸甲锁已闭合，正面装甲免伤 75%！凭你那把破铆钉枪，连我的外层涂装都刮不花！",
          },
          {
            speaker: "vela",
            name: "林顿·薇拉 (Vela)",
            role: "首席整备师 · 灰烬信标",
            text: "别硬拼正面装甲！它的反应炉冷却锁每过几秒就会因为过热自动弹开，或者引诱避难所脉冲震开胸口核心锁——抓紧蓝色核心暴露窗口集火输出！",
          },
        ],
      },
      {
        id: "epilogue",
        actLabel: "EPILOGUE // FIN",
        title: "终幕：灰烬之上",
        location: "锈锚盆地 · 晨曦高塔",
        lines: [
          {
            speaker: "kael",
            name: "凯尔 (Kael)",
            role: "R-17 拾荒铁骑驾驶员",
            text: "铁冠领主的胸口反应炉彻底熄火了……这片废土的天空，好久没这么亮过了。",
          },
          {
            speaker: "vela",
            name: "林顿·薇拉 (Vela)",
            role: "首席整备师 · 灰烬信标",
            text: "干得漂亮，凯尔！避难所熔炉已经全功率运转，把最后这批高纯度核心运回来，今晚整备班给你换一套全新的镀金液压臂！",
          },
        ],
      },
    ];

    // =========================================================================
    // 3. MECHA HANGAR 5 UNITS x 4 POSES (Reconstructed from src/game/hangar.ts)
    // =========================================================================
    const HANGAR_UNITS = [
      {
        id: "r17",
        code: "UNIT-01 // R-17",
        name: "R-17 拾荒铁骑 · 铆钉号",
        role: "主角驾驶机体 · 重型拾荒突击铁骑",
        armor: "铆接复合钢 + 旋转磁盾",
        reactor: "双回路高压蒸汽核",
        weapon: "32mm 铆钉机炮 / 震荡锤 / 电弧枪",
        lore: "由灰烬信标首席整备师薇拉利用旧世代工程机底盘与战列舰副炮液压件改装而成的全地形履带铁骑。左臂搭载三段式旋转磁力护盾，右臂集成液压退壳铆钉机炮，背负双联蒸汽锅炉与超载散热翼。",
        callouts: [
          { part: "双肩超载散热翼", desc: "Overdrive 激活时自动展开 24° 并高频脉动排热", x: 0.5, y: 0.22 },
          { part: "左臂三段旋转磁盾", desc: "3 段式青色等离子电弧环持续旋转偏折弹道", x: 0.28, y: 0.56 },
          { part: "右臂液压退壳机炮", desc: "开火时枪管后座 12px 并向上抛射黄铜弹壳", x: 0.76, y: 0.48 },
          { part: "全地形履带防滑齿", desc: "底部啮合齿随前进相位实时滚动并扬起烟尘", x: 0.5, y: 0.78 },
        ],
      },
      {
        id: "scuttler",
        code: "UNIT-02 // SCUTTLER",
        name: "掘进锯蟹 · 撕裂者",
        role: "高速近战突袭集群 · 矿道拆解机",
        armor: "轻型赤褐防爆壳",
        reactor: "高转冲压微型涡轮",
        weapon: "前置八齿高速钨钢圆锯",
        lore: "原本用于自动化矿道掘进的六足机械蟹，被铁冠中枢刷写敌我识别逻辑后化为疯狂的近战集群。两侧三对铰接机械足按交替三角步态高频摆动，车头高速旋转的钨钢圆锯能瞬间切穿轻型护甲。",
        callouts: [
          { part: "前置八齿钨钢圆锯", desc: "14 rad/s 高速旋转切割轮，带切削火花", x: 0.38, y: 0.48 },
          { part: "六足交替三角步态", desc: "左右 3 对机械足按正弦相位差交替迈步", x: 0.65, y: 0.64 },
        ],
      },
      {
        id: "brute",
        code: "UNIT-03 // BRUTE",
        name: "铁砧重锤机 · 粉碎者",
        role: "重甲攻城前卫 · 双联液压冲击臂",
        armor: "加厚铸铁正面胸甲",
        reactor: "重油增压活塞炉",
        weapon: "双联万吨液压攻城锤",
        lore: "专为强拆地下掩体设计的重型履带装甲体。正面覆盖厚重的焦茶色铸铁装甲板，双臂安装大行程液压冲击柱塞，在攻击与超载姿态下可释放环形地面震波。",
        callouts: [
          { part: "正面加厚铸铁胸甲", desc: "高额生命值，破盾姿态下显现橙红裂纹", x: 0.5, y: 0.42 },
          { part: "双联液压冲击柱塞", desc: "随攻击节拍大幅往复伸缩并激起地面震波环", x: 0.25, y: 0.56 },
        ],
      },
      {
        id: "zapper",
        code: "UNIT-04 // ZAPPER",
        name: "浮游电弧台 · 磁暴棱镜",
        role: "中程游走火力支援 · 反重力放电核心",
        armor: "轻质绝缘陶瓷翼",
        reactor: "冷聚变电离环",
        weapon: "高压追踪电弧束",
        lore: "悬浮于战场中后排的无人电离信标。三片呈 120° 对称排布的散热翼围绕中央青绿电离核心呼吸脉动，锁定目标后拉出高穿深虚线瞄准激光并释放连锁闪电。",
        callouts: [
          { part: "三翼对称散热阵列", desc: "随反重力悬浮相位上下浮动与微倾", x: 0.32, y: 0.36 },
          { part: "中央青绿电离球核", desc: "外圈谐振磁环高频缩放，攻击时投射瞄准线", x: 0.55, y: 0.52 },
        ],
      },
      {
        id: "boss",
        code: "UNIT-05 // IRON CROWN BOSS",
        name: "铁冠领主 · 典狱官重机",
        role: "第三幕关底首领 · 胸甲锁弱点机制巨兽",
        armor: "铁冠重工超重型反应炉胸甲 (闭锁减伤75%)",
        reactor: "铁冠六螺栓拘束核反应炉",
        weapon: "双联重型液压巨臂 + 环形弹幕发生器",
        lore: "统御锈锚盆地的巨型攻城指挥机。常规状态下胸口的六螺栓铁冠反应炉处于严密闭锁状态（减伤 75%）；当进入『弱点破盾 Lock-Break』阶段时，六颗拘束螺栓向外弹开高速旋转，暴露出湛蓝反应炉核心（承受 2.5× 暴击伤害）。",
        callouts: [
          { part: "二阶段超载排热翼", desc: "进入狂暴阶段后双肩赤红排热翼展开", x: 0.24, y: 0.28 },
          { part: "铁冠六螺栓胸甲锁", desc: "闭锁时赤红免伤；破盾时蓝核暴露 + 六螺栓飞旋", x: 0.5, y: 0.48 },
          { part: "重型四轮履带底盘", desc: "超宽攻城履带底座提供极高抗击退稳定性", x: 0.5, y: 0.74 },
        ],
      },
    ];

    const HANGAR_POSES = [
      { id: "cruise", label: "巡航待机 (Cruise)" },
      { id: "attack", label: "战术开火 (Attack)" },
      { id: "overdrive", label: "蒸汽超载 (Overdrive)" },
      { id: "lockbreak", label: "弱点破盾 (Lock-Break)" },
    ];

    // Procedural Multi-Joint Mecha Drawers (used in both Hangar & Combat Arena!)
    function drawMechaR17(ctx, cx, cy, scale, pose, t) {
      const isOverdrive = pose === "overdrive" || pose === "lockbreak";
      const isAttack = pose === "attack" || pose === "overdrive";
      const bob = Math.sin(t * 7) * 3.5;
      const lean = isAttack ? 0.08 : Math.sin(t * 3.5) * 0.03;

      ctx.save();
      ctx.translate(cx, cy + bob * scale);
      ctx.scale(scale, scale);
      ctx.rotate(lean);

      // Overdrive radiator fins
      if (isOverdrive) {
        ctx.fillStyle = "#e7ad4b";
        ctx.strokeStyle = "#29251d";
        ctx.lineWidth = 2;
        for (const side of [-1, 1]) {
          ctx.save();
          ctx.translate(side * 34, -36);
          ctx.rotate(side * (0.42 + Math.sin(t * 10) * 0.08));
          ctx.fillRect(-7, -22, 14, 24);
          ctx.strokeRect(-7, -22, 14, 24);
          ctx.restore();
        }
      }

      // Backpack & Steam Plumes
      ctx.fillStyle = "#3c4237";
      ctx.strokeStyle = "#1c1f1a";
      ctx.lineWidth = 3;
      ctx.fillRect(-52, -38, 24, 58);
      ctx.strokeRect(-52, -38, 24, 58);
      ctx.fillStyle = "#8f5a32";
      ctx.fillRect(-46, -54, 14, 18);
      for (let i = 0; i < 3; i++) {
        const phase = (t * 2.2 + i * 0.33) % 1;
        ctx.fillStyle = isOverdrive
          ? \`rgba(231, 173, 75, \${(1 - phase) * 0.5})\`
          : \`rgba(210, 195, 155, \${(1 - phase) * 0.35})\`;
        ctx.beginPath();
        ctx.arc(-39 - phase * 18, -60 - phase * 34, 6 + phase * 10, 0, Math.PI * 2);
        ctx.fill();
      }

      // Treads & scrolling cleats
      ctx.fillStyle = "#20231f";
      ctx.strokeStyle = "#0e100d";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.roundRect(-42, 22, 84, 34, 12);
      ctx.fill();
      ctx.stroke();
      for (const wx of [-22, 22]) {
        ctx.fillStyle = "#7d7458";
        ctx.beginPath();
        ctx.arc(wx, 39, 11, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#23251f";
        ctx.lineWidth = 2;
        const spoke = t * 6;
        ctx.beginPath();
        ctx.moveTo(wx + Math.cos(spoke) * 9, 39 + Math.sin(spoke) * 9);
        ctx.lineTo(wx - Math.cos(spoke) * 9, 39 - Math.sin(spoke) * 9);
        ctx.stroke();
      }
      const cleatShift = Math.floor(t * 28) % 12;
      ctx.strokeStyle = "#c3a86a";
      ctx.lineWidth = 2.5;
      for (let ox = -32; ox <= 28; ox += 12) {
        ctx.beginPath();
        ctx.moveTo(ox + cleatShift - 6, 53);
        ctx.lineTo(ox + cleatShift, 56);
        ctx.stroke();
      }

      // Torso
      ctx.fillStyle = "#76785e";
      ctx.strokeStyle = "#252821";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.roundRect(-32, -32, 64, 58, 10);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#b7863d";
      ctx.beginPath();
      ctx.moveTo(-24, 18);
      ctx.lineTo(24, 18);
      ctx.lineTo(0, -20);
      ctx.closePath();
      ctx.fill();

      // Left Magnetic Shield Arm + Rotating Energy Ring
      const shieldAng = t * 4.5;
      ctx.strokeStyle = "#5d6251";
      ctx.lineWidth = 11;
      ctx.beginPath();
      ctx.moveTo(-28, -14);
      ctx.lineTo(-48, 12);
      ctx.stroke();
      ctx.fillStyle = "#2b322a";
      ctx.beginPath();
      ctx.arc(-52, 18, 17, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#00e5ff";
      ctx.lineWidth = 3;
      for (let arcIdx = 0; arcIdx < 3; arcIdx++) {
        const start = shieldAng + (arcIdx * Math.PI * 2) / 3;
        ctx.beginPath();
        ctx.arc(-52, 18, 22, start, start + 1.2);
        ctx.stroke();
      }

      // Head & Visor
      ctx.fillStyle = "#595f50";
      ctx.strokeStyle = "#22251f";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.roundRect(-25, -66, 50, 32, 8);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#141e17";
      ctx.fillRect(-18, -56, 36, 13);
      ctx.fillStyle = isOverdrive ? "#ffcc38" : "#b9dd78";
      ctx.fillRect(-12, -52, 26, 5);

      // Right Rivet Cannon Arm + Hydraulic Recoil + Brass Shell Ejection
      const recoilCycle = isAttack ? Math.max(0, Math.sin(t * 16)) * 12 : 0;
      ctx.strokeStyle = "#656957";
      ctx.lineWidth = 11;
      ctx.beginPath();
      ctx.moveTo(28, -16);
      ctx.lineTo(48 - recoilCycle * 0.4, 2);
      ctx.stroke();

      const gunX = 44 - recoilCycle;
      ctx.fillStyle = "#484e45";
      ctx.strokeStyle = "#20231e";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.roundRect(gunX, -6, 50, 18, 4);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#c48438";
      ctx.fillRect(gunX + 44, -2, 12, 10);

      if (isAttack && recoilCycle > 5) {
        const mx = gunX + 62;
        const my = 3;
        ctx.strokeStyle = "#ffe28a";
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(mx - 14, my);
        ctx.lineTo(mx + 18, my);
        ctx.moveTo(mx, my - 14);
        ctx.lineTo(mx, my + 14);
        ctx.stroke();

        const shellPhase = (t * 8) % 1;
        const sx = gunX + 16 - shellPhase * 28;
        const sy = -10 - Math.sin(shellPhase * Math.PI) * 32;
        ctx.save();
        ctx.translate(sx, sy);
        ctx.rotate(shellPhase * 9);
        ctx.fillStyle = "#f2b84b";
        ctx.fillRect(-4, -2, 8, 4);
        ctx.restore();
      }
      ctx.restore();
    }

    function drawMechaScuttler(ctx, cx, cy, scale, pose, t) {
      const speed = pose === "overdrive" || pose === "attack" ? 14 : 8;
      const gait = Math.sin(t * speed) * 9;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(scale, scale);
      ctx.strokeStyle = "#52402e";
      ctx.lineWidth = 6;
      ctx.lineCap = "round";
      for (let i = 0; i < 3; i++) {
        const alt = i % 2 === 0 ? gait : -gait;
        const y0 = -14 + i * 14;
        ctx.beginPath();
        ctx.moveTo(-16, y0);
        ctx.lineTo(-46 + alt, y0 + 8);
        ctx.lineTo(-58 + alt * 0.5, y0 + 24);
        ctx.moveTo(16, y0);
        ctx.lineTo(46 - alt, y0 + 8);
        ctx.lineTo(58 - alt * 0.5, y0 + 24);
        ctx.stroke();
      }
      ctx.fillStyle = "#733928";
      ctx.strokeStyle = "#2b211b";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.ellipse(0, 0, 44, 28, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      const sawX = -20;
      const sawY = -2;
      ctx.fillStyle = "#282824";
      ctx.beginPath();
      ctx.arc(sawX, sawY, 17, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#d99d45";
      ctx.lineWidth = 3;
      for (let k = 0; k < 8; k++) {
        const a = (k * Math.PI) / 4 + t * 14;
        ctx.beginPath();
        ctx.moveTo(sawX + Math.cos(a) * 11, sawY + Math.sin(a) * 11);
        ctx.lineTo(sawX + Math.cos(a) * 22, sawY + Math.sin(a) * 22);
        ctx.stroke();
      }
      ctx.fillStyle = "#ffae42";
      ctx.beginPath();
      ctx.arc(16, -5, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }

    function drawMechaBrute(ctx, cx, cy, scale, pose, t) {
      const isSlam = pose === "attack" || pose === "overdrive";
      const isDamaged = pose === "lockbreak" || pose === "overdrive";
      const piston = Math.sin(t * (isSlam ? 9 : 4)) * (isSlam ? 10 : 4);

      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(scale, scale);
      if (isSlam) {
        ctx.strokeStyle = "rgba(240, 179, 79, 0.55)";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(0, 10, 68 + Math.sin(t * 12) * 8, 0, Math.PI * 2);
        ctx.stroke();
      }
      ctx.fillStyle = "#20211d";
      ctx.beginPath();
      ctx.roundRect(-48, 16, 96, 32, 10);
      ctx.fill();
      ctx.fillStyle = "#745038";
      ctx.strokeStyle = "#2c2820";
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.roundRect(-38, -38, 76, 62, 8);
      ctx.fill();
      ctx.stroke();

      if (isDamaged) {
        ctx.strokeStyle = "#ff7838";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(-22, -24);
        ctx.lineTo(-6, -8);
        ctx.lineTo(-14, 8);
        ctx.stroke();
      }

      ctx.strokeStyle = "#66543d";
      ctx.lineWidth = 14;
      ctx.beginPath();
      ctx.moveTo(-36, -18);
      ctx.lineTo(-62 - piston, 12);
      ctx.moveTo(36, -18);
      ctx.lineTo(62 + piston, 12);
      ctx.stroke();

      ctx.fillStyle = "#f0b34f";
      ctx.fillRect(-18, -26, 36, 8);
      ctx.restore();
    }

    function drawMechaZapper(ctx, cx, cy, scale, pose, t) {
      const hover = Math.sin(t * 5) * 7;
      const tilt = Math.cos(t * 3.5) * 0.1;
      ctx.save();
      ctx.translate(cx, cy + hover * scale);
      ctx.scale(scale, scale);
      ctx.rotate(tilt);

      ctx.fillStyle = "#56625c";
      ctx.strokeStyle = "#2c3531";
      ctx.lineWidth = 3;
      for (const dir of [-1, 1]) {
        ctx.beginPath();
        ctx.moveTo(dir * 18, -6);
        ctx.lineTo(dir * 62, -24);
        ctx.lineTo(dir * 48, 18);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }
      ctx.beginPath();
      ctx.moveTo(0, -22);
      ctx.lineTo(-14, -54);
      ctx.lineTo(14, -54);
      ctx.closePath();
      ctx.fill();

      ctx.fillStyle = "#28302e";
      ctx.beginPath();
      ctx.arc(0, 0, 26, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#9cd7c8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(0, 0, 34 + Math.sin(t * 10) * 3, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = "#b9f4c9";
      ctx.beginPath();
      ctx.arc(0, 0, 9, 0, Math.PI * 2);
      ctx.fill();

      if (pose === "attack" || pose === "overdrive") {
        ctx.strokeStyle = "rgba(185, 244, 201, 0.8)";
        ctx.setLineDash([6, 5]);
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(95, 42);
        ctx.stroke();
        ctx.setLineDash([]);
      }
      ctx.restore();
    }

    function drawMechaBoss(ctx, cx, cy, scale, pose, t) {
      const isPhase2 = pose === "overdrive" || pose === "attack" || pose === "lockbreak";
      const isLockBreak = pose === "lockbreak";
      const piston = Math.sin(t * 4) * 7;

      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(scale, scale);

      if (isPhase2) {
        ctx.fillStyle = "#b8442a";
        ctx.strokeStyle = "#ffb548";
        ctx.lineWidth = 2.5;
        for (const side of [-1, 1]) {
          ctx.save();
          ctx.translate(side * 48, -36);
          ctx.rotate(side * (0.35 + Math.sin(t * 6) * 0.06));
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.lineTo(side * 38, -26);
          ctx.lineTo(side * 30, 14);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
          ctx.restore();
        }
      }

      ctx.fillStyle = "#22231e";
      ctx.strokeStyle = "#0e0f0d";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.roundRect(-68, 18, 136, 36, 12);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#756344";
      for (let x = -48; x <= 48; x += 24) {
        ctx.beginPath();
        ctx.arc(x, 36, 10, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = "#5d4632";
      ctx.strokeStyle = "#29251d";
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.roundRect(-48, -42, 96, 64, 10);
      ctx.fill();
      ctx.stroke();

      ctx.strokeStyle = "#655038";
      ctx.lineWidth = 12;
      ctx.beginPath();
      ctx.moveTo(-44, -20);
      ctx.lineTo(-74 - piston, 6);
      ctx.moveTo(44, -20);
      ctx.lineTo(74 + piston, 6);
      ctx.stroke();

      const lockRadius = isLockBreak ? 26 : 22;
      ctx.fillStyle = "#24261f";
      ctx.beginPath();
      ctx.arc(0, -4, lockRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = isLockBreak ? "#00e5ff" : "#d65b35";
      ctx.lineWidth = 4;
      ctx.stroke();

      const spin = t * (isLockBreak ? 10 : 1.5);
      for (let b = 0; b < 6; b++) {
        const a = (b * Math.PI) / 3 + spin;
        const dist = isLockBreak ? 23 + Math.sin(t * 14) * 3 : 17;
        ctx.fillStyle = isLockBreak ? "#ffe28a" : "#b8975c";
        ctx.beginPath();
        ctx.arc(Math.cos(a) * dist, -4 + Math.sin(a) * dist, 3.5, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.fillStyle = isLockBreak ? "#00e5ff" : "#e0a044";
      ctx.beginPath();
      ctx.arc(0, -4, isLockBreak ? 11 : 7, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = "#242a24";
      ctx.strokeStyle = "#9a7a43";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.roundRect(-24, -64, 48, 26, 6);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#ffb548";
      ctx.fillRect(-16, -54, 32, 6);

      ctx.restore();
    }

    // =========================================================================
    // 4. REA AST COMPARISON DATA (Minified Bundle vs Reconstructed TypeScript)
    // =========================================================================
    const AST_MODULES = {
      hangar: {
        minified: \`function Jt(e,t,n,r,a){const i=r==="overdrive"||r==="lockbreak",s=r==="attack"||r==="overdrive",o=Math.sin(a*7)*3.5;e.save(),e.translate(t,n+o),i&&[-1,1].forEach(c=>{e.save(),e.translate(c*34,-36),e.rotate(c*(.42+Math.sin(a*10)*.08)),e.fillRect(-7,-22,14,24),e.restore()});const l=s?Math.max(0,Math.sin(a*16))*12:0;e.roundRect(44-l,-6,50,18,4),e.restore()}\`,
        decompiled: \`// Reconstructed from Jt() in index-Da3qZ_pX.js
export function drawHangarR17(ctx: CanvasRenderingContext2D, cx: number, cy: number, pose: HangarPoseId, t: number) {
  const isOverdrive = pose === "overdrive" || pose === "lockbreak";
  const isAttack = pose === "attack" || pose === "overdrive";
  const bob = Math.sin(t * 7) * 3.5;
  // Dual shoulder radiator fins + 3-segment magnetic shield + brass shell ejection
  const recoilCycle = isAttack ? Math.max(0, Math.sin(t * 16)) * 12 : 0;
  ctx.roundRect(44 - recoilCycle, -6, 50, 18, 4);
}\`,
      },
      data: {
        minified: \`const Wt=[{id:"rivet_cannon",key:"1",cd:.14,dmg:18,spd:680},{id:"shock_hammer",key:"2",cd:.58,dmg:42,aoe:118},{id:"arc_tether",key:"3",cd:.28,dmg:24,chains:3}],Kt={hp:1400,armorMul:.25,exposeMul:2.5,exposeSec:4.5};\`,
        decompiled: \`// Reconstructed Weapon & Boss Lock Table (src/game/data.ts)
export const WEAPON_SPECS = [
  { id: "rivet_cannon", key: "1", cooldown: 0.14, damage: 18, speed: 680 },
  { id: "shock_hammer", key: "2", cooldown: 0.58, damage: 42, radius: 118 },
  { id: "arc_tether",   key: "3", cooldown: 0.28, damage: 24, chains: 3 },
];
export const BOSS_SPEC = { hp: 1400, armoredMultiplier: 0.25, exposedMultiplier: 2.5, exposeSec: 4.5 };\`,
      },
      story: {
        minified: \`const Xt={overdrive:{speaker:"kael",title:"“蒸汽超载阀全开——撕碎敌阵！”"},boss_lock_open:{speaker:"vela",title:"“铁冠胸口核心锁已弹开！集火蓝色弱点！”"}};\`,
        decompiled: \`// Reconstructed Cut-In & 5-Chapter Narrative Specs (src/game/story.ts)
export const CUTIN_SPECS: Record<CutinId, CutinSpec> = {
  overdrive: { speaker: "kael", title: "“蒸汽超载阀全开——撕碎敌阵！”" },
  boss_lock_open: { speaker: "vela", title: "“铁冠胸口核心锁已弹开！集火蓝色弱点！”" },
};\`,
      },
      audio: {
        minified: \`class Zt{tone(e,t,n,r="sawtooth",a=.05,i=0){const s=this.ensure();if(!s)return;const o=s.currentTime+i,l=s.createOscillator(),c=s.createGain();l.type=r,l.frequency.setValueAtTime(e,o),l.frequency.exponentialRampToValueAtTime(t,o+n),l.connect(c),c.connect(s.destination),l.start(o),l.stop(o+n)}}\`,
        decompiled: \`// Reconstructed Zero-Asset Web Audio Synthesizer (src/game/audio.ts)
export class ProceduralAudioEngine {
  tone(f0: number, f1: number, dur: number, type: OscillatorType = "sawtooth", gain = 0.05) {
    const osc = ctx.createOscillator();
    osc.frequency.setValueAtTime(Math.max(24, f0), t0);
    osc.frequency.exponentialRampToValueAtTime(Math.max(24, f1), t0 + dur);
  }
}\`,
      },
      prng: {
        minified: \`function qt(e){let t=e>>>0||2463534242;return()=>{t^=t<<13,t^=t>>>17,t^=t<<5;return(t>>>0)/4294967296}}\`,
        decompiled: \`// Reconstructed Deterministic xorshift32 PRNG (src/game/prng.ts)
export function createXorShift32(seed = 0x92d68ca2): () => number {
  let state = seed >>> 0 || 2463534242;
  return () => {
    state ^= state << 13; state ^= state >>> 17; state ^= state << 5;
    return (state >>> 0) / 4294967296;
  };
}\`,
      },
      physics: {
        minified: \`function Yt(e,t,n){const r=t.x-e.x,a=t.y-e.y,i=Math.hypot(r,a)||1;if(i<n){const s=(n-i)/i*.5;e.x-=r*s,e.y-=a*s,t.x+=r*s,t.y+=a*s}}\`,
        decompiled: \`// Reconstructed Circle-Circle Knockback & Separation Solver (src/game/physics.ts)
export function resolveCircleImpulse(a: Vec2, b: Vec2, minDist: number): void {
  const dx = b.x - a.x, dy = b.y - a.y;
  const dist = Math.hypot(dx, dy) || 1;
  if (dist < minDist) {
    const push = ((minDist - dist) / dist) * 0.5;
    a.x -= dx * push; a.y -= dy * push;
    b.x += dx * push; b.y += dy * push;
  }
}\`,
      },
      director: {
        minified: \`function Gt(e){return e<45?{act:1,cap:12,boss:!1}:e<110?{act:2,cap:24,boss:!1}:{act:3,cap:32,boss:!0}}\`,
        decompiled: \`// Reconstructed Wave Director & Act Escalation State Machine (src/game/director.ts)
export function evaluateWaveBudget(elapsedSec: number): WaveBudget {
  if (elapsedSec < 45)  return { act: 1, maxSwarm: 12, spawnIronCrown: false };
  if (elapsedSec < 110) return { act: 2, maxSwarm: 24, spawnIronCrown: false };
  return { act: 3, maxSwarm: 32, spawnIronCrown: true };
}\`,
      },
      spatial: {
        minified: \`function Vt(e,t,n){for(const r of e){const a=t.x-r.x,i=t.y-r.y,s=Math.hypot(a,i);s<n&&(r.x+=a/s*220,r.y+=i/s*220)}}\`,
        decompiled: \`// Reconstructed Magnetic Scrap Tractor-Beam Solver (src/game/spatial.ts)
export function pullScrapOrbsWithinRadius(orbs: ScrapOrb[], player: Vec2, magnetRadius = 155, dt = 1/60): void {
  for (const orb of orbs) {
    const dx = player.x - orb.x, dy = player.y - orb.y, dist = Math.hypot(dx, dy);
    if (dist < magnetRadius && dist > 1) {
      orb.x += (dx / dist) * 220 * dt; orb.y += (dy / dist) * 220 * dt;
    }
  }
}\`,
      },
      combat: {
        minified: \`function Ht(e,t,n){const r=t?1.6:1,a=n?.exposed?2.5:n?.isBoss?.25:1;return Math.round(e*r*a)}\`,
        decompiled: \`// Reconstructed Armor Mitigation & Boss Weakpoint Multiplier (src/game/combat.ts)
export function computeDamageWithArmor(baseDmg: number, isOverdrive: boolean, target: { isBoss?: boolean; exposed?: boolean }): number {
  const overdriveMul = isOverdrive ? 1.6 : 1.0;
  const armorMul = target.exposed ? 2.5 : target.isBoss ? 0.25 : 1.0;
  return Math.round(baseDmg * overdriveMul * armorMul);
}\`,
      },
      save: {
        minified: \`const Qt="scrap-swarm-save-v1";function Bt(){try{const e=JSON.parse(localStorage.getItem(Qt)||"{}");return{scrap:e.scrap|0,bestAct:Math.max(1,e.bestAct|0),upgrades:e.upgrades||{}}}catch{return{scrap:0,bestAct:1,upgrades:{}}}}\`,
        decompiled: \`// Reconstructed LocalStorage Save Profile & Sanitizer (src/game/save.ts)
export const SAVE_KEY = "scrap-swarm-save-v1";
export function loadOrInitSaveProfile(): SaveProfile {
  try {
    const raw = JSON.parse(localStorage.getItem(SAVE_KEY) || "{}");
    return { scrap: raw.scrap | 0, bestAct: Math.max(1, raw.bestAct | 0), upgrades: raw.upgrades ?? {} };
  } catch {
    return { scrap: 0, bestAct: 1, upgrades: {} };
  }
}\`,
      },
      hud: {
        minified: \`function Nt(e,t){return{actLabel:t?t.exposed?"BOSS // WEAKPOINT OPEN":"BOSS // ARMOR 75%":"ACT I-II // SWARM",overdrivePct:Math.min(1,e.overdriveTimer/e.overdriveMax)}}\`,
        decompiled: \`// Reconstructed Tactical HUD State Formatter (src/game/hud.ts)
export function formatTacticalReadout(player: PlayerState, boss: BossState | null): HudReadout {
  return {
    actLabel: boss ? (boss.exposed ? "BOSS // WEAKPOINT OPEN" : "BOSS // ARMOR 75%") : "ACT I-II // SWARM",
    overdrivePct: Math.min(1, player.overdriveTimer / player.overdriveMax),
  };
}\`,
      },
    };

    // =========================================================================
    // 5. UI WIRING: TABS, HANGAR, STORY THEATER, AST & SOUNDBOARD
    // =========================================================================
    const tabBtns = document.querySelectorAll(".tab-btn");
    const panes = {
      arena: document.getElementById("pane-arena"),
      hangar: document.getElementById("pane-hangar"),
      story: document.getElementById("pane-story"),
    };
    tabBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        tabBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        Object.values(panes).forEach((p) => p.classList.remove("active"));
        panes[btn.dataset.tab].classList.add("active");
        audio.play("hit");
      });
    });

    // AST Module Switcher
    const minBox = document.getElementById("minifiedCodeBox");
    const decBox = document.getElementById("decompiledCodeBox");
    function setAstModule(mod) {
      minBox.textContent = AST_MODULES[mod].minified;
      decBox.textContent = AST_MODULES[mod].decompiled;
    }
    setAstModule("hangar");
    document.querySelectorAll("#astModuleBtns button").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll("#astModuleBtns button").forEach((b) => b.classList.remove("primary"));
        btn.classList.add("primary");
        setAstModule(btn.dataset.ast);
      });
    });

    // Soundboard Grid
    const sfxList = [
      ["shot", "铆钉射击"],
      ["pulse", "震荡铁锤"],
      ["arc", "电弧连锁"],
      ["dash", "推进冲刺"],
      ["hit", "装甲受击"],
      ["kill", "敌机击毁"],
      ["shelterPulse", "避难所EMP"],
      ["lockExpose", "铁冠破盾"],
      ["cutin", "特写警报"],
      ["winFanfare", "战役凯旋"],
    ];
    const sbGrid = document.getElementById("soundboardGrid");
    sfxList.forEach(([id, label]) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "sfx-btn";
      b.textContent = "🔊 " + label;
      b.addEventListener("click", () => audio.play(id));
      sbGrid.appendChild(b);
    });

    // Hangar UI Wiring
    let activeHangarUnit = HANGAR_UNITS[0];
    let activeHangarPose = "cruise";
    let hangarXray = false;
    const unitBtnsWrap = document.getElementById("hangarUnitBtns");
    const poseBtnsWrap = document.getElementById("hangarPoseBtns");
    const btnHangarXray = document.getElementById("btnHangarXray");
    if (btnHangarXray) {
      btnHangarXray.addEventListener("click", () => {
        hangarXray = !hangarXray;
        btnHangarXray.classList.toggle("primary", hangarXray);
        audio.play("arc");
        pulseEvidence("hangar");
      });
    }

    function updateHangarMeta() {
      document.getElementById("hangarRole").textContent = activeHangarUnit.code + " · " + activeHangarUnit.role;
      document.getElementById("hangarName").textContent = activeHangarUnit.name;
      document.getElementById("hangarArmor").textContent = activeHangarUnit.armor;
      document.getElementById("hangarReactor").textContent = activeHangarUnit.reactor;
      document.getElementById("hangarWeapon").textContent = activeHangarUnit.weapon;
      document.getElementById("hangarLore").textContent = activeHangarUnit.lore;
      const calloutsEl = document.getElementById("hangarCallouts");
      calloutsEl.innerHTML = activeHangarUnit.callouts
        .map((c, idx) => \`<div class="hangar-callout-item"><strong>[0\${idx + 1}] \${c.part}</strong>\${c.desc}</div>\`)
        .join("");
    }

    HANGAR_UNITS.forEach((u, idx) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "act-btn" + (idx === 0 ? " primary" : "");
      b.textContent = u.name.split(" · ")[0];
      b.addEventListener("click", () => {
        activeHangarUnit = u;
        unitBtnsWrap.querySelectorAll("button").forEach((x) => x.classList.remove("primary"));
        b.classList.add("primary");
        updateHangarMeta();
        audio.play("dash");
      });
      unitBtnsWrap.appendChild(b);
    });

    HANGAR_POSES.forEach((p, idx) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "act-btn" + (idx === 0 ? " primary" : "");
      b.textContent = p.label;
      b.addEventListener("click", () => {
        activeHangarPose = p.id;
        poseBtnsWrap.querySelectorAll("button").forEach((x) => x.classList.remove("primary"));
        b.classList.add("primary");
        audio.play(p.id === "lockbreak" ? "lockExpose" : "shot");
      });
      poseBtnsWrap.appendChild(b);
    });
    updateHangarMeta();

    // Story Theater Tab Wiring
    let selectedChapterIdx = 0;
    const chapterBtnsWrap = document.getElementById("storyChapterBtns");
    function renderStoryTheater() {
      const ch = STORY_CHAPTERS[selectedChapterIdx];
      document.getElementById("storyChapterHeader").innerHTML = \`
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <span style="font-family:var(--mono);font-size:11px;color:var(--accent);font-weight:700">\${ch.actLabel}</span>
            <h3 style="font-size:17px;color:#fff;margin-top:2px">\${ch.title}</h3>
          </div>
          <span style="font-family:var(--mono);font-size:11px;color:var(--muted)">📍 \${ch.location}</span>
        </div>
      \`;
      document.getElementById("storyLinesContainer").innerHTML = ch.lines
        .map(
          (line, i) => \`
        <div class="dialogue-row \${i === 0 ? "highlight" : ""}">
          <div class="story-portrait">\${speakerBadgeSvg(line.speaker)}</div>
          <div style="flex:1">
            <div>
              <span class="story-speaker-name">\${line.name}</span>
              <span class="story-speaker-role">\${line.role}</span>
            </div>
            <div class="story-text">\${line.text}</div>
          </div>
        </div>
      \`
        )
        .join("");
    }
    STORY_CHAPTERS.forEach((ch, idx) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "act-btn" + (idx === 0 ? " primary" : "");
      b.textContent = ch.title;
      b.addEventListener("click", () => {
        selectedChapterIdx = idx;
        chapterBtnsWrap.querySelectorAll("button").forEach((x) => x.classList.remove("primary"));
        b.classList.add("primary");
        renderStoryTheater();
        audio.play("hit");
      });
      chapterBtnsWrap.appendChild(b);
    });
    renderStoryTheater();

    const cutinPreviewWrap = document.getElementById("cutinPreviewBtns");
    Object.entries(CUTIN_SPECS).forEach(([key, spec]) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "act-btn";
      b.textContent = "⚡ " + spec.speakerTag.split(" · ")[1];
      b.addEventListener("click", () => {
        tabBtns[0].click();
        showCutin(key);
      });
      cutinPreviewWrap.appendChild(b);
    });

    // =========================================================================
    // 6. CUT-IN BANNER & INTERACTIVE STORY OVERLAY IN ARENA
    // =========================================================================
    let cutinTimer = 0;
    function showCutin(kind) {
      const spec = CUTIN_SPECS[kind] || CUTIN_SPECS.overdrive;
      document.getElementById("cutinAvatar").innerHTML = speakerBadgeSvg(spec.speaker);
      document.getElementById("cutinSpeaker").textContent = spec.speakerTag;
      document.getElementById("cutinTitle").textContent = spec.title;
      document.getElementById("cutinSub").textContent = spec.subtitle;
      const banner = document.getElementById("cutinBanner");
      banner.classList.add("show");
      cutinTimer = 3.2;
      audio.play("cutin");
    }

    let modalChapter = null;
    let modalLineIdx = 0;
    const storyOverlay = document.getElementById("storyOverlay");

    function openStoryModal(chapterIdx) {
      modalChapter = STORY_CHAPTERS[chapterIdx] || STORY_CHAPTERS[0];
      modalLineIdx = 0;
      storyOverlay.classList.add("active");
      updateStoryModalLine();
      audio.play("cutin");
    }
    function updateStoryModalLine() {
      if (!modalChapter) return;
      const line = modalChapter.lines[modalLineIdx];
      document.getElementById("modalStoryAct").textContent = modalChapter.actLabel + " · " + modalChapter.title;
      document.getElementById("modalStoryLoc").textContent = modalChapter.location;
      document.getElementById("modalStoryPortrait").innerHTML = speakerBadgeSvg(line.speaker);
      document.getElementById("modalStorySpeaker").textContent = line.name;
      document.getElementById("modalStoryRole").textContent = line.role;
      document.getElementById("modalStoryText").textContent = line.text;
      document.getElementById("modalStoryStep").textContent = \`LINE \${modalLineIdx + 1} / \${modalChapter.lines.length}\`;
    }
    document.getElementById("btnNextStory").addEventListener("click", () => {
      if (!modalChapter) return;
      modalLineIdx++;
      if (modalLineIdx >= modalChapter.lines.length) {
        storyOverlay.classList.remove("active");
        modalChapter = null;
      } else {
        updateStoryModalLine();
        audio.play("hit");
      }
    });
    document.getElementById("btnSkipStory").addEventListener("click", () => {
      storyOverlay.classList.remove("active");
      modalChapter = null;
    });
    document.getElementById("btnPlayChapterInArena").addEventListener("click", () => {
      tabBtns[0].click();
      openStoryModal(selectedChapterIdx);
    });

    // =========================================================================
    // 7. PLAYABLE ARENA + LIVE MEMORY HOT-PATCH ENGINE
    // =========================================================================
    const gameCanvas = document.getElementById("gameCanvas");
    const gCtx = gameCanvas.getContext("2d");
    const hangarCanvas = document.getElementById("hangarCanvas");
    const hCtx = hangarCanvas.getContext("2d");

    // Hot-patchable runtime config
    const livePatch = {
      moveSpeed: 245,
      fireRateScale: 1.0,
      bossExposeSec: 4.5,
      magnetRadius: 175,
      arcChainCount: 3,
      overdriveDuration: 6.0,
    };

    document.getElementById("patchSpeed").addEventListener("input", (e) => {
      livePatch.moveSpeed = Number(e.target.value);
      document.getElementById("valSpeed").textContent = livePatch.moveSpeed + " px/s";
    });
    document.getElementById("patchFireRate").addEventListener("input", (e) => {
      livePatch.fireRateScale = Number(e.target.value);
      document.getElementById("valFireRate").textContent = livePatch.fireRateScale.toFixed(2) + "×";
    });
    document.getElementById("patchBossExpose").addEventListener("input", (e) => {
      livePatch.bossExposeSec = Number(e.target.value);
      document.getElementById("valBossExpose").textContent = livePatch.bossExposeSec.toFixed(1) + " s";
    });
    const patchMagnetEl = document.getElementById("patchMagnet");
    if (patchMagnetEl) {
      patchMagnetEl.addEventListener("input", (e) => {
        livePatch.magnetRadius = Number(e.target.value);
        document.getElementById("valMagnet").textContent = livePatch.magnetRadius + " px";
        pulseEvidence("emp");
      });
    }
    const patchArcChainEl = document.getElementById("patchArcChain");
    if (patchArcChainEl) {
      patchArcChainEl.addEventListener("input", (e) => {
        livePatch.arcChainCount = Number(e.target.value);
        document.getElementById("valArcChain").textContent = livePatch.arcChainCount + " 跳";
        pulseEvidence("weapon");
      });
    }
    const patchOverdriveDurEl = document.getElementById("patchOverdriveDur");
    if (patchOverdriveDurEl) {
      patchOverdriveDurEl.addEventListener("input", (e) => {
        livePatch.overdriveDuration = Number(e.target.value);
        document.getElementById("valOverdriveDur").textContent = livePatch.overdriveDuration.toFixed(1) + " s";
        pulseEvidence("hangar");
      });
    }

    const weapons = [
      { id: "rivet", name: "铆钉机炮 [1]", cd: 0.16 },
      { id: "hammer", name: "震荡铁锤 [2]", cd: 0.55 },
      { id: "arc", name: "串联电弧枪 [3]", cd: 0.30 },
    ];
    let weaponIdx = 0;
    let autoPlay = true;
    let gameClock = 0;

    const player = {
      x: 480,
      y: 320,
      hp: 120,
      shield: 45,
      scrap: 24,
      overdriveTimer: 0,
      fireTimer: 0,
    };

    const bullets = [];
    const particles = [];
    const dmgPopups = [];
    const shockRings = [];
    const lightningArcs = [];
    const scrapOrbs = [];
    const shellCasings = [];
    const enemyBolts = [];
    const enemies = [
      { kind: "scuttler", x: 180, y: 150, hp: 60, maxHp: 60 },
      { kind: "scuttler", x: 780, y: 160, hp: 60, maxHp: 60 },
      { kind: "brute", x: 210, y: 470, hp: 140, maxHp: 140 },
      { kind: "zapper", x: 760, y: 450, hp: 90, maxHp: 90 },
    ];
    let boss = null;

    function spawnBoss() {
      boss = {
        x: 480,
        y: 125,
        hp: 1400,
        maxHp: 1400,
        exposed: false,
        timer: 3.5,
      };
      showCutin("boss_entry");
      document.getElementById("hudAct").textContent = "ACT III · 铁冠降临";
    }

    function pulseEvidence(evKey) {
      const el = document.querySelector(\`.ev-item[data-ev="\${evKey}"]\`);
      if (!el) return;
      el.classList.add("pulse");
      setTimeout(() => el.classList.remove("pulse"), 520);
    }

    let empWaveRadius = 0;
    function triggerShelterEmp() {
      empWaveRadius = 20;
      player.shield = 60;
      showCutin("shelter");
      audio.play("shelterPulse");
      pulseEvidence("emp");
      pulseEvidence("audio");
      for (const e of enemies) {
        const ang = Math.atan2(e.y - 320, e.x - 480);
        e.x = Math.max(50, Math.min(910, e.x + Math.cos(ang) * 110));
        e.y = Math.max(50, Math.min(550, e.y + Math.sin(ang) * 110));
        e.hp -= 35;
        dmgPopups.push({ x: e.x, y: e.y - 26, text: "EMP -35", color: "#00e5ff", life: 0.75 });
      }
      if (boss) {
        boss.exposed = true;
        boss.timer = livePatch.bossExposeSec;
        pulseEvidence("boss");
      }
    }

    const afterimages = [];
    function triggerDash() {
      for (let i = 0; i < 4; i++) {
        afterimages.push({ x: player.x, y: player.y, life: 0.28 - i * 0.05 });
      }
      const ang = Math.random() * Math.PI * 2;
      player.x = Math.max(80, Math.min(880, player.x + Math.cos(ang) * 95));
      player.y = Math.max(80, Math.min(520, player.y + Math.sin(ang) * 95));
      audio.play("dash");
      pulseEvidence("hangar");
    }

    const keys = {};
    window.addEventListener("keydown", (e) => {
      keys[e.key.toLowerCase()] = true;
      if (e.key === "1") weaponIdx = 0;
      if (e.key === "2") weaponIdx = 1;
      if (e.key === "3") weaponIdx = 2;
      if (e.key === " ") {
        e.preventDefault();
        triggerDash();
      }
      if (e.key.toLowerCase() === "q") triggerOverdrive();
      if (e.key.toLowerCase() === "e") triggerShelterEmp();
    });
    window.addEventListener("keyup", (e) => {
      keys[e.key.toLowerCase()] = false;
    });

    function triggerOverdrive() {
      player.overdriveTimer = livePatch.overdriveDuration;
      showCutin("overdrive");
      pulseEvidence("hangar");
      pulseEvidence("story");
    }

    document.getElementById("btnAutoPlay").addEventListener("click", (e) => {
      autoPlay = !autoPlay;
      e.target.textContent = autoPlay ? "🤖 AI 自动巡航演示: ON" : "🕹️ 手动键鼠操控: ON";
      e.target.classList.toggle("primary", autoPlay);
    });
    document.getElementById("btnSwitchWeapon").addEventListener("click", () => {
      weaponIdx = (weaponIdx + 1) % weapons.length;
      audio.play("dash");
      pulseEvidence("weapon");
    });
    document.getElementById("btnDash").addEventListener("click", () => triggerDash());
    document.getElementById("btnTriggerOverdrive").addEventListener("click", () => triggerOverdrive());
    document.getElementById("btnShelterEmp").addEventListener("click", () => triggerShelterEmp());
    document.getElementById("btnSpawnBoss").addEventListener("click", () => {
      spawnBoss();
      pulseEvidence("boss");
    });
    const cutinKeys = ["overdrive", "shelter", "boss_entry", "boss_lock_open"];
    let cutinCycleIdx = 0;
    document.getElementById("btnTriggerCutin").addEventListener("click", () => {
      showCutin(cutinKeys[cutinCycleIdx % cutinKeys.length]);
      cutinCycleIdx++;
    });
    document.getElementById("btnOpenPrologue").addEventListener("click", () => openStoryModal(0));

    function updateArena(dt) {
      gameClock += dt;
      if (cutinTimer > 0) {
        cutinTimer -= dt;
        if (cutinTimer <= 0) {
          document.getElementById("cutinBanner").classList.remove("show");
        }
      }
      if (player.overdriveTimer > 0) player.overdriveTimer = Math.max(0, player.overdriveTimer - dt);

      // Movement (AI Patrol or WASD)
      if (autoPlay) {
        const targetX = 480 + Math.cos(gameClock * 0.9) * 210;
        const targetY = 340 + Math.sin(gameClock * 1.3) * 135;
        const dx = targetX - player.x;
        const dy = targetY - player.y;
        const dist = Math.hypot(dx, dy) || 1;
        const step = Math.min(dist, livePatch.moveSpeed * dt);
        player.x += (dx / dist) * step;
        player.y += (dy / dist) * step;
      } else {
        let vx = (keys["d"] ? 1 : 0) - (keys["a"] ? 1 : 0);
        let vy = (keys["s"] ? 1 : 0) - (keys["w"] ? 1 : 0);
        const len = Math.hypot(vx, vy) || 1;
        if (vx || vy) {
          player.x = Math.max(60, Math.min(900, player.x + (vx / len) * livePatch.moveSpeed * dt));
          player.y = Math.max(60, Math.min(540, player.y + (vy / len) * livePatch.moveSpeed * dt));
        }
      }

      // Maintain enemy wave population
      if (enemies.length < 4) {
        const types = ["scuttler", "brute", "zapper"];
        const kind = types[Math.floor(Math.random() * types.length)];
        const angle = Math.random() * Math.PI * 2;
        enemies.push({
          kind,
          x: 480 + Math.cos(angle) * 390,
          y: 300 + Math.sin(angle) * 230,
          hp: kind === "brute" ? 140 : 75,
          maxHp: kind === "brute" ? 140 : 75,
        });
      }

      // Boss state machine + 6-way radial siege plasma ring barrage
      if (boss) {
        boss.timer -= dt;
        if (boss.timer <= 0) {
          boss.exposed = !boss.exposed;
          boss.timer = boss.exposed ? livePatch.bossExposeSec : 4.2;
          if (boss.exposed) showCutin("boss_lock_open");
        }
        boss.barrageTimer = (boss.barrageTimer || 2.4) - dt;
        if (boss.barrageTimer <= 0) {
          boss.barrageTimer = 2.6;
          shockRings.push({ x: boss.x, y: boss.y, r: 18, maxR: 84, life: 0.34 });
          for (let k = 0; k < 6; k++) {
            const a = (k * Math.PI) / 3 + gameClock * 0.6;
            enemyBolts.push({
              x: boss.x + Math.cos(a) * 26,
              y: boss.y + Math.sin(a) * 26,
              vx: Math.cos(a) * 215,
              vy: Math.sin(a) * 215,
              life: 2.4,
            });
          }
          pulseEvidence("boss");
        }
        boss.x = 480 + Math.sin(gameClock * 0.7) * 180;
      }

      // Weapon auto-fire toward nearest target
      player.fireTimer -= dt * livePatch.fireRateScale * (player.overdriveTimer > 0 ? 1.85 : 1);
      const allTargets = boss ? [boss, ...enemies] : enemies;
      if (player.fireTimer <= 0 && allTargets.length > 0) {
        const w = weapons[weaponIdx];
        player.fireTimer = w.cd;
        let nearest = allTargets[0];
        let bestD = Infinity;
        for (const t of allTargets) {
          const d = Math.hypot(t.x - player.x, t.y - player.y);
          if (d < bestD) {
            bestD = d;
            nearest = t;
          }
        }
        const ang = Math.atan2(nearest.y - player.y, nearest.x - player.x);
        bullets.push({
          x: player.x + Math.cos(ang) * 28,
          y: player.y + Math.sin(ang) * 28,
          vx: Math.cos(ang) * 620,
          vy: Math.sin(ang) * 620,
          kind: w.id,
          life: 1.1,
        });
        const ejectAng = ang - Math.PI * 0.55 + (Math.random() - 0.5) * 0.4;
        shellCasings.push({
          x: player.x + Math.cos(ang) * 14,
          y: player.y + Math.sin(ang) * 14,
          vx: Math.cos(ejectAng) * (65 + Math.random() * 45),
          vy: Math.sin(ejectAng) * (65 + Math.random() * 45) - 35,
          rot: Math.random() * Math.PI,
          vrot: (Math.random() - 0.5) * 18,
          life: 0.75,
        });
      }

      // Update bullets
      for (let i = bullets.length - 1; i >= 0; i--) {
        const b = bullets[i];
        b.x += b.vx * dt;
        b.y += b.vy * dt;
        b.life -= dt;
        let hit = false;
        if (boss && Math.hypot(b.x - boss.x, b.y - boss.y) < 48) {
          const dmg = boss.exposed ? 45 : 7;
          boss.hp -= dmg;
          hit = true;
          dmgPopups.push({
            x: boss.x + (Math.random() - 0.5) * 32,
            y: boss.y - 42,
            text: boss.exposed ? "CRIT -" + dmg + "!" : "-" + dmg,
            color: boss.exposed ? "#00e5ff" : "#b8ad96",
            life: 0.65,
          });
          for (let k = 0; k < 4; k++) {
            particles.push({
              x: b.x,
              y: b.y,
              vx: (Math.random() - 0.5) * 160,
              vy: (Math.random() - 0.5) * 160,
              color: boss.exposed ? "#00e5ff" : "#f0b34f",
              life: 0.35,
            });
          }
          if (boss.hp <= 0) {
            boss = null;
            player.scrap += 150;
            audio.play("winFanfare");
          }
        }
        for (let j = enemies.length - 1; j >= 0 && !hit; j--) {
          const e = enemies[j];
          if (Math.hypot(b.x - e.x, b.y - e.y) < 34) {
            const isCrit = player.overdriveTimer > 0;
            const dmg = isCrit ? 42 : 26;
            e.hp -= dmg;
            hit = true;
            if (b.kind === "hammer") {
              shockRings.push({ x: e.x, y: e.y, r: 10, maxR: 92, life: 0.32 });
            } else if (b.kind === "arc" && enemies.length > 1) {
              let prev = e;
              for (let c = 1; c < livePatch.arcChainCount; c++) {
                const next = enemies[(j + c) % enemies.length];
                if (next && next !== prev) {
                  next.hp -= 16;
                  lightningArcs.push({ x1: prev.x, y1: prev.y, x2: next.x, y2: next.y, life: 0.24 });
                  prev = next;
                }
              }
            }
            dmgPopups.push({
              x: e.x + (Math.random() - 0.5) * 20,
              y: e.y - 28,
              text: isCrit ? "CRIT -" + dmg + "!" : "-" + dmg,
              color: isCrit ? "#ffb548" : "#ffe28a",
              life: 0.55,
            });
            particles.push({
              x: b.x,
              y: b.y,
              vx: (Math.random() - 0.5) * 140,
              vy: (Math.random() - 0.5) * 140,
              color: "#ffe28a",
              life: 0.3,
            });
            if (e.hp <= 0) {
              scrapOrbs.push({
                x: e.x,
                y: e.y,
                core: Math.random() < 0.28,
                val: e.kind === "brute" ? 18 : 10,
              });
              enemies.splice(j, 1);
            }
          }
        }
        if (hit || b.life <= 0) bullets.splice(i, 1);
      }

      // Magnetic Scrap Orb & Overdrive Cell Tractor Beam
      for (let i = scrapOrbs.length - 1; i >= 0; i--) {
        const orb = scrapOrbs[i];
        const dx = player.x - orb.x;
        const dy = player.y - orb.y;
        const dist = Math.hypot(dx, dy) || 1;
        if (dist < livePatch.magnetRadius) {
          orb.x += (dx / dist) * 235 * dt;
          orb.y += (dy / dist) * 235 * dt;
        }
        if (dist < 26) {
          player.scrap += orb.val;
          if (orb.core) {
            player.hp = Math.min(120, player.hp + 5);
          }
          dmgPopups.push({
            x: player.x,
            y: player.y - 34,
            text: orb.core ? "+CORE +5HP" : "+" + orb.val + " SCRAP",
            color: orb.core ? "#00e5ff" : "#b9dd78",
            life: 0.55,
          });
          scrapOrbs.splice(i, 1);
        }
      }
      for (let i = shellCasings.length - 1; i >= 0; i--) {
        const sc = shellCasings[i];
        sc.x += sc.vx * dt;
        sc.y += sc.vy * dt;
        sc.vy += 180 * dt;
        sc.rot += sc.vrot * dt;
        sc.life -= dt;
        if (sc.life <= 0) shellCasings.splice(i, 1);
      }

      // Update enemies & Zapper/Boss ranged plasma bolts deflected by R-17 Magnetic Shield
      for (const e of enemies) {
        const ang = Math.atan2(player.y - e.y, player.x - e.x);
        const spd = e.kind === "scuttler" ? 68 : e.kind === "brute" ? 38 : 28;
        e.x += Math.cos(ang) * spd * dt;
        e.y += Math.sin(ang) * spd * dt;
        if (e.kind === "zapper" && Math.random() < dt * 0.55) {
          enemyBolts.push({
            x: e.x,
            y: e.y,
            vx: Math.cos(ang) * 260,
            vy: Math.sin(ang) * 260,
            life: 2.2,
          });
        }
      }
      for (let i = enemyBolts.length - 1; i >= 0; i--) {
        const eb = enemyBolts[i];
        eb.x += eb.vx * dt;
        eb.y += eb.vy * dt;
        eb.life -= dt;
        if (Math.hypot(eb.x - player.x, eb.y - player.y) < 34) {
          dmgPopups.push({
            x: player.x - 18,
            y: player.y - 30,
            text: "SHIELD DEFLECT",
            color: "#00e5ff",
            life: 0.48,
          });
          for (let k = 0; k < 4; k++) {
            particles.push({
              x: eb.x,
              y: eb.y,
              vx: (Math.random() - 0.5) * 150,
              vy: (Math.random() - 0.5) * 150,
              color: "#00e5ff",
              life: 0.28,
            });
          }
          enemyBolts.splice(i, 1);
          continue;
        }
        if (eb.life <= 0) enemyBolts.splice(i, 1);
      }

      // Update particles & floating damage numbers
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.life -= dt;
        if (p.life <= 0) particles.splice(i, 1);
      }
      for (let i = dmgPopups.length - 1; i >= 0; i--) {
        const dp = dmgPopups[i];
        dp.y -= 28 * dt;
        dp.life -= dt;
        if (dp.life <= 0) dmgPopups.splice(i, 1);
      }

      // HUD refresh
      document.getElementById("hudHp").textContent = \`\${player.hp} / \${player.shield}\`;
      document.getElementById("hudWeapon").textContent = weapons[weaponIdx].name;
      document.getElementById("hudOverdrive").textContent =
        player.overdriveTimer > 0 ? \`ACTIVE (\${player.overdriveTimer.toFixed(1)}s)\` : "READY [Q]";
      document.getElementById("hudScrap").textContent = String(player.scrap);
      document.getElementById("hudBoss").textContent = boss
        ? \`\${Math.max(0, Math.round(boss.hp))} HP (\${boss.exposed ? "🔓 破盾2.5×" : "🔒 闭锁75%减伤"})\`
        : "点击召唤 [Boss]";
    }

    function renderArena() {
      gCtx.fillStyle = "#141812";
      gCtx.fillRect(0, 0, 960, 600);

      // Tactical Wasteland Grid & Shelter Beacon Circle
      gCtx.strokeStyle = "rgba(180, 190, 160, 0.06)";
      gCtx.lineWidth = 1;
      for (let x = 0; x <= 960; x += 48) {
        gCtx.beginPath();
        gCtx.moveTo(x, 0);
        gCtx.lineTo(x, 600);
        gCtx.stroke();
      }
      for (let y = 0; y <= 600; y += 48) {
        gCtx.beginPath();
        gCtx.moveTo(0, y);
        gCtx.lineTo(960, y);
        gCtx.stroke();
      }

      // Shelter magnetic ring & Central Ashen Beacon Nano-Repair Tether in center
      gCtx.strokeStyle = "rgba(0, 229, 255, 0.18)";
      gCtx.lineWidth = 2;
      gCtx.setLineDash([8, 6]);
      gCtx.beginPath();
      gCtx.arc(480, 320, 95 + Math.sin(gameClock * 2.5) * 4, 0, Math.PI * 2);
      gCtx.stroke();
      gCtx.setLineDash([]);
      gCtx.fillStyle = "rgba(0, 229, 255, 0.22)";
      gCtx.beginPath();
      gCtx.arc(480, 320, 12, 0, Math.PI * 2);
      gCtx.fill();
      if (Math.hypot(player.x - 480, player.y - 320) < 175) {
        gCtx.strokeStyle = "rgba(82, 229, 168, 0.35)";
        gCtx.lineWidth = 2;
        gCtx.setLineDash([6, 4]);
        gCtx.beginPath();
        gCtx.moveTo(480, 320);
        gCtx.lineTo(player.x, player.y);
        gCtx.stroke();
        gCtx.setLineDash([]);
      }

      if (empWaveRadius > 0) {
        empWaveRadius += 14;
        gCtx.strokeStyle = \`rgba(0, 229, 255, \${Math.max(0, 1 - empWaveRadius / 460)})\`;
        gCtx.lineWidth = 5;
        gCtx.beginPath();
        gCtx.arc(480, 320, empWaveRadius, 0, Math.PI * 2);
        gCtx.stroke();
        if (empWaveRadius > 460) empWaveRadius = 0;
      }

      // Draw enemies using procedural multi-joint mecha drawers
      for (const e of enemies) {
        if (e.kind === "scuttler") drawMechaScuttler(gCtx, e.x, e.y, 0.56, "attack", gameClock);
        else if (e.kind === "brute") drawMechaBrute(gCtx, e.x, e.y, 0.62, "attack", gameClock);
        else drawMechaZapper(gCtx, e.x, e.y, 0.62, "attack", gameClock);

        // HP bar
        gCtx.fillStyle = "rgba(0,0,0,0.65)";
        gCtx.fillRect(e.x - 24, e.y - 38, 48, 5);
        gCtx.fillStyle = "#e25a3c";
        gCtx.fillRect(e.x - 24, e.y - 38, 48 * Math.max(0, e.hp / e.maxHp), 5);
      }

      // Draw Boss if active
      if (boss) {
        drawMechaBoss(gCtx, boss.x, boss.y, 0.92, boss.exposed ? "lockbreak" : "overdrive", gameClock);
        gCtx.fillStyle = "rgba(0,0,0,0.75)";
        gCtx.fillRect(boss.x - 65, boss.y - 74, 130, 8);
        gCtx.fillStyle = boss.exposed ? "#00e5ff" : "#f0b34f";
        gCtx.fillRect(boss.x - 65, boss.y - 74, 130 * Math.max(0, boss.hp / boss.maxHp), 8);
      }

      // Draw Afterimages & Player R-17 Mecha
      for (let i = afterimages.length - 1; i >= 0; i--) {
        const a = afterimages[i];
        a.life -= 1 / 60;
        if (a.life <= 0) {
          afterimages.splice(i, 1);
          continue;
        }
        gCtx.save();
        gCtx.globalAlpha = Math.max(0.1, a.life * 1.8);
        drawMechaR17(gCtx, a.x, a.y, 0.66, "overdrive", gameClock);
        gCtx.restore();
      }
      drawMechaR17(
        gCtx,
        player.x,
        player.y,
        0.68,
        player.overdriveTimer > 0 ? "overdrive" : "attack",
        gameClock
      );

      // Draw Magnetic Scrap Alloy Orbs & Tractor-Beam Tethers + Ejected Brass Shell Casings
      gCtx.strokeStyle = "rgba(0, 229, 255, 0.11)";
      gCtx.lineWidth = 1;
      gCtx.setLineDash([4, 6]);
      gCtx.beginPath();
      gCtx.arc(player.x, player.y, livePatch.magnetRadius, 0, Math.PI * 2);
      gCtx.stroke();
      gCtx.setLineDash([]);
      for (const sc of shellCasings) {
        gCtx.save();
        gCtx.translate(sc.x, sc.y);
        gCtx.rotate(sc.rot);
        gCtx.fillStyle = "#e0b354";
        gCtx.fillRect(-3, -1.3, 6, 2.6);
        gCtx.restore();
      }
      for (const orb of scrapOrbs) {
        const dist = Math.hypot(player.x - orb.x, player.y - orb.y);
        if (dist < livePatch.magnetRadius) {
          gCtx.strokeStyle = "rgba(0, 229, 255, 0.28)";
          gCtx.lineWidth = 1.5;
          gCtx.setLineDash([4, 4]);
          gCtx.beginPath();
          gCtx.moveTo(orb.x, orb.y);
          gCtx.lineTo(player.x, player.y);
          gCtx.stroke();
          gCtx.setLineDash([]);
        }
        gCtx.fillStyle = orb.core ? "#00e5ff" : "#f0b34f";
        gCtx.beginPath();
        gCtx.arc(orb.x, orb.y, orb.core ? 6.5 : 5, 0, Math.PI * 2);
        gCtx.fill();
      }

      // Draw Bullets, Shock Hammer AoE Rings & Arc Tether Chain Lightning
      for (let i = shockRings.length - 1; i >= 0; i--) {
        const sr = shockRings[i];
        sr.r += (sr.maxR - sr.r) * 0.22;
        sr.life -= 1 / 60;
        if (sr.life <= 0) {
          shockRings.splice(i, 1);
          continue;
        }
        gCtx.strokeStyle = \`rgba(240, 179, 79, \${Math.max(0, sr.life * 2.8)})\`;
        gCtx.lineWidth = 3;
        gCtx.beginPath();
        gCtx.arc(sr.x, sr.y, sr.r, 0, Math.PI * 2);
        gCtx.stroke();
      }
      for (let i = lightningArcs.length - 1; i >= 0; i--) {
        const la = lightningArcs[i];
        la.life -= 1 / 60;
        if (la.life <= 0) {
          lightningArcs.splice(i, 1);
          continue;
        }
        gCtx.strokeStyle = \`rgba(0, 229, 255, \${Math.max(0, la.life * 4)})\`;
        gCtx.lineWidth = 2.5;
        gCtx.beginPath();
        gCtx.moveTo(la.x1, la.y1);
        gCtx.lineTo((la.x1 + la.x2) * 0.5 + (Math.random() - 0.5) * 24, (la.y1 + la.y2) * 0.5 + (Math.random() - 0.5) * 24);
        gCtx.lineTo(la.x2, la.y2);
        gCtx.stroke();
      }
      for (const b of bullets) {
        gCtx.fillStyle = b.kind === "arc" ? "#00e5ff" : b.kind === "hammer" ? "#f0b34f" : "#ffe28a";
        gCtx.beginPath();
        gCtx.arc(b.x, b.y, b.kind === "hammer" ? 7 : 4.5, 0, Math.PI * 2);
        gCtx.fill();
      }
      for (const eb of enemyBolts) {
        gCtx.fillStyle = "#ff5c77";
        gCtx.beginPath();
        gCtx.arc(eb.x, eb.y, 4.2, 0, Math.PI * 2);
        gCtx.fill();
      }

      // Draw Particles & Floating Damage Popups
      for (const p of particles) {
        gCtx.fillStyle = p.color;
        gCtx.fillRect(p.x - 2, p.y - 2, 4, 4);
      }
      gCtx.font = "800 12px 'JetBrains Mono', monospace";
      gCtx.textAlign = "center";
      for (const dp of dmgPopups) {
        gCtx.save();
        gCtx.globalAlpha = Math.max(0, Math.min(1, dp.life * 1.8));
        gCtx.fillStyle = dp.color;
        gCtx.fillText(dp.text, dp.x, dp.y);
        gCtx.restore();
      }
    }

    function renderHangarPreview() {
      hCtx.fillStyle = "#10130e";
      hCtx.fillRect(0, 0, 580, 400);

      // Blueprint grid
      hCtx.strokeStyle = "rgba(0, 229, 255, 0.08)";
      hCtx.lineWidth = 1;
      for (let x = 0; x <= 580; x += 36) {
        hCtx.beginPath();
        hCtx.moveTo(x, 0);
        hCtx.lineTo(x, 400);
        hCtx.stroke();
      }
      for (let y = 0; y <= 400; y += 36) {
        hCtx.beginPath();
        hCtx.moveTo(0, y);
        hCtx.lineTo(580, y);
        hCtx.stroke();
      }

      // Turntable ring
      hCtx.strokeStyle = "rgba(240, 179, 79, 0.35)";
      hCtx.lineWidth = 2;
      hCtx.beginPath();
      hCtx.ellipse(290, 275, 135, 36, 0, 0, Math.PI * 2);
      hCtx.stroke();

      const u = activeHangarUnit.id;
      if (u === "r17") drawMechaR17(hCtx, 290, 210, 1.55, activeHangarPose, gameClock);
      else if (u === "scuttler") drawMechaScuttler(hCtx, 290, 220, 1.65, activeHangarPose, gameClock);
      else if (u === "brute") drawMechaBrute(hCtx, 290, 215, 1.55, activeHangarPose, gameClock);
      else if (u === "zapper") drawMechaZapper(hCtx, 290, 210, 1.6, activeHangarPose, gameClock);
      else if (u === "boss") drawMechaBoss(hCtx, 290, 215, 1.45, activeHangarPose, gameClock);

      if (hangarXray) {
        hCtx.save();
        hCtx.strokeStyle = "rgba(0, 229, 255, 0.78)";
        hCtx.lineWidth = 1.6;
        hCtx.setLineDash([5, 4]);
        hCtx.beginPath();
        hCtx.arc(290, 212, u === "boss" ? 92 : 66, 0, Math.PI * 2);
        hCtx.stroke();
        hCtx.setLineDash([]);
        hCtx.fillStyle = "rgba(0, 229, 255, 0.22)";
        hCtx.beginPath();
        hCtx.arc(290, 212, 16 + Math.sin(gameClock * 8) * 3, 0, Math.PI * 2);
        hCtx.fill();
        hCtx.fillStyle = "#00e5ff";
        hCtx.font = "bold 10px monospace";
        hCtx.fillText("REA HITBOX & REACTOR CORE X-RAY", 198, 108);
        hCtx.restore();
      }

      // Blueprint Callout Pins
      activeHangarUnit.callouts.forEach((c, idx) => {
        const px = c.x * 580;
        const py = c.y * 400;
        hCtx.fillStyle = "#00e5ff";
        hCtx.beginPath();
        hCtx.arc(px, py, 5, 0, Math.PI * 2);
        hCtx.fill();
        hCtx.fillStyle = "#ffe28a";
        hCtx.font = "bold 11px monospace";
        hCtx.fillText(\`[0\${idx + 1}] \${c.part}\`, px + 9, py + 4);
      });
    }

    let lastTime = 0;
    function loop(now) {
      const dt = lastTime ? Math.min((now - lastTime) / 1000, 0.05) : 1 / 60;
      lastTime = now;
      updateArena(dt);
      renderArena();
      renderHangarPreview();
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
  </script>
</body>
</html>`;

const outPath = join(HERE, "index.html");
writeFileSync(outPath, html, "utf8");
console.log("wrote", outPath);
