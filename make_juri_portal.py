import os
from pathlib import Path

html_code = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fit Code — Yeşilay İzmir Sağlıklı Yaşam Ligi Jüri Portalı</title>
  <style>
    :root {
      --bg-dark: #0a1811;
      --card-bg: rgba(18, 44, 31, 0.75);
      --card-border: #225a3d;
      --accent-green: #2ecc71;
      --accent-lime: #b5df62;
      --brand-green: #44b78b;
      --text-main: #f0f7f3;
      --text-muted: #8ea89a;
      --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-dark);
      background-image: radial-gradient(circle at 50% 0%, #153826 0%, #0a1811 75%);
      color: var(--text-main);
      font-family: var(--font-stack);
      line-height: 1.5;
      padding-bottom: 60px;
    }
    a { color: var(--accent-lime); text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* Top Bar */
    .top-header {
      background: rgba(11, 28, 20, 0.95);
      border-bottom: 2px solid var(--card-border);
      padding: 14px 25px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(10px);
    }
    .brand-logos { display: flex; align-items: center; gap: 18px; }
    .brand-logos img { height: 42px; object-fit: contain; }
    .brand-title h1 { font-size: 19px; font-weight: 800; color: var(--brand-green); letter-spacing: 0.5px; }
    .brand-title p { font-size: 12px; color: var(--text-muted); }
    .offline-badge {
      background: #19442e;
      border: 1px solid var(--accent-lime);
      color: var(--accent-lime);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .offline-badge::before {
      content: "";
      display: inline-block;
      width: 8px;
      height: 8px;
      background: var(--accent-lime);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--accent-lime);
    }

    /* Container */
    .container { max-width: 1200px; margin: 25px auto; padding: 0 20px; }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, rgba(26, 77, 54, 0.9), rgba(15, 38, 27, 0.95));
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 30px;
      margin-bottom: 25px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }
    .hero-text h2 { font-size: 26px; color: #fff; margin-bottom: 8px; }
    .hero-text h2 span { color: var(--accent-lime); }
    .hero-text p { font-size: 14px; color: #b7cebf; max-width: 720px; }
    .hero-team {
      background: rgba(10, 24, 17, 0.7);
      border: 1px solid var(--brand-green);
      padding: 16px 22px;
      border-radius: 12px;
      font-size: 13px;
    }
    .hero-team strong { color: var(--accent-lime); display: block; margin-bottom: 4px; font-size: 14px; }

    /* Navigation Tabs */
    .nav-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      margin-bottom: 25px;
      border-bottom: 1px solid var(--card-border);
    }
    .tab-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 10px 18px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tab-btn:hover { background: rgba(46, 204, 113, 0.15); color: #fff; border-color: var(--brand-green); }
    .tab-btn.active {
      background: var(--brand-green);
      color: #0a1811;
      border-color: var(--brand-green);
      font-weight: 800;
      box-shadow: 0 4px 15px rgba(68, 183, 139, 0.35);
    }

    /* Tab Contents */
    .tab-content { display: none; }
    .tab-content.active { display: block; animation: fadeIn 0.3s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* Cards & Grids */
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .card-title {
      font-size: 17px;
      font-weight: 700;
      color: var(--brand-green);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn {
      display: inline-block;
      padding: 10px 20px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 14px;
      cursor: pointer;
      border: none;
      transition: all 0.2s ease;
      text-align: center;
    }
    .btn-primary { background: var(--brand-green); color: #0a1811; }
    .btn-primary:hover { background: var(--accent-lime); }
    .btn-outline {
      background: transparent;
      border: 1px solid var(--brand-green);
      color: var(--brand-green);
    }
    .btn-outline:hover { background: rgba(68, 183, 139, 0.15); color: #fff; }

    /* HANGMAN GAME STYLES */
    .game-board {
      background: rgba(10, 24, 17, 0.85);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 25px;
    }
    .word-boxes { display: flex; flex-wrap: wrap; gap: 8px; margin: 20px 0; min-height: 55px; }
    .word-box {
      width: 48px; height: 58px;
      background: rgba(68, 183, 139, 0.15);
      border: 2px solid var(--brand-green);
      border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      font-size: 28px; font-weight: 800; color: #fff;
    }
    .keyboard { display: flex; flex-wrap: wrap; gap: 6px; max-width: 650px; }
    .key-btn {
      width: 42px; height: 42px;
      background: #173827; border: 1px solid #295c40;
      color: #fff; border-radius: 8px; font-size: 15px; font-weight: 700;
      cursor: pointer;
    }
    .key-btn:hover:not(:disabled) { background: var(--brand-green); color: #0a1811; }
    .key-btn:disabled { background: #1a2520; color: #53645c; border-color: #24332c; cursor: not-allowed; }
    .hint-box {
      background: rgba(46, 204, 113, 0.12);
      border-left: 4px solid var(--accent-green);
      padding: 14px 18px;
      border-radius: 8px;
      margin: 15px 0;
      font-size: 15px;
    }

    /* TABU GAME STYLES */
    .tabu-card {
      background: linear-gradient(135deg, #133324, #1b4934);
      border: 2px solid var(--brand-green);
      border-radius: 16px;
      padding: 25px;
      text-align: center;
      max-width: 420px;
      margin: 0 auto;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .tabu-target { font-size: 30px; font-weight: 900; color: var(--accent-lime); margin: 12px 0; }
    .tabu-forbidden {
      background: rgba(0,0,0,0.3);
      border-radius: 10px;
      padding: 15px;
      margin-top: 15px;
      text-align: left;
    }
    .tabu-forbidden h4 { color: #e74c3c; font-size: 13px; margin-bottom: 8px; text-transform: uppercase; }
    .tabu-forbidden ul { list-style: none; }
    .tabu-forbidden li { padding: 4px 0; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 16px; font-weight: 600; }

    /* LABYRINTH STYLES */
    #mazeCanvas { background: #0a1811; border: 2px solid var(--brand-green); border-radius: 12px; display: block; margin: 10px auto; }

    /* PDF IFRAME */
    .pdf-viewer-frame {
      width: 100%;
      height: 700px;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      background: #111;
    }

    @media (max-width: 768px) {
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
      .brand-title p { display: none; }
    }
  </style>
</head>
<body>

  <!-- Top Bar -->
  <header class="top-header">
    <div class="brand-logos">
      <img src="offline_assets/img/yesil_logo.png" alt="Yeşilay" onerror="this.style.display='none'">
      <img src="offline_assets/img/meb_logo.png" alt="MEB" onerror="this.style.display='none'">
      <img src="offline_assets/img/zs_logo.png" alt="ZŞMTAL" onerror="this.style.display='none'">
      <div class="brand-title">
        <h1>FIT CODE · SPOR KOÇ & İYİLİK ROTASI</h1>
        <p>Karşıyaka Zeki Şairoğlu MTAL · Yeşilay İzmir Sağlıklı Yaşam Ligi</p>
      </div>
    </div>
    <div class="offline-badge">
      %100 ÇEVRİMDIŞI ÇALIŞIYOR (SIFIR KURULUM)
    </div>
  </header>

  <div class="container">

    <!-- Hero Banner -->
    <section class="hero-banner">
      <div class="hero-text">
        <h2>Yeşilay İzmir Sağlıklı Yaşam Ligi <span>Jüri Değerlendirme Portalı</span></h2>
        <p>Bu portal; jüri üyelerimizin internet bağlantısı, Python veya herhangi bir ek yazılım kurmasına gerek kalmadan, projemizin haftalık resmî kanıt dosyalarını incelemesi ve tüm interaktif oyunları/modülleri canlı deneyimlemesi için hazırlanmıştır.</p>
      </div>
      <div class="hero-team">
        <strong>FIT CODE TAKIMI (ATP 10/A)</strong>
        <div>Emir Can KÖKLÜ (5114)</div>
        <div>Kerem KELEŞOĞLU (5108)</div>
        <div>Seçkin Ege AK (5113)</div>
        <div style="margin-top:6px; color:#8ea89a;">Danışman: Demet AYDEMİR</div>
        <div style="color:#8ea89a;">Müdür: Ali TOPRAK</div>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab('tab-ozet')">📌 Genel Özet & 3 Aşamalı Model</button>
      <button class="tab-btn" onclick="switchTab('tab-pdf')">📄 Resmî Kanıt Dosyaları (PDF)</button>
      <button class="tab-btn" onclick="switchTab('tab-oyun')">🎮 Sağlıklı Yaşam Oyunu (Adam Asmaca)</button>
      <button class="tab-btn" onclick="switchTab('tab-tabu')">🃏 Hareket Tabu (62 Kart)</button>
      <button class="tab-btn" onclick="switchTab('tab-labirent')">🧭 Sağlıklı Yaşam Labirenti</button>
      <button class="tab-btn" onclick="switchTab('tab-hesap')">⚖️ Sağlık Hesaplayıcıları</button>
      <button class="tab-btn" onclick="switchTab('tab-iyilik')">🗺️ İyilik Rotası QR Görevleri</button>
      <button class="tab-btn" onclick="switchTab('tab-kodlar')">🔒 Şifreli Kaynak Kodlar</button>
    </nav>

    <!-- TAB 1: GENEL ÖZET -->
    <div id="tab-ozet" class="tab-content active">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">🏆 Proje Amacı ve Tematik Uyum</div>
          <p style="color:#d1e0d7; margin-bottom:12px;">Fit Code projemiz; Yeşilay misyonu doğrultusunda sağlıklı yaşam alışkanlıklarını (düzenli hareket, dengeli beslenme, kaliteli uyku, dijital denge ve hijyen) bireysel sorumluluktan toplumsal bir iyilik hareketine dönüştürmeyi amaçlar.</p>
          <ul style="padding-left: 20px; color: var(--text-muted); font-size: 14px; margin-bottom: 15px;">
            <li><strong>1. Tema (Sorumluluk ve İyilik Hâli):</strong> Okul temizlik görevlilerine yardım, atık ayrıştırma ve vefa söyleşisi (Zor Düzey 50 Puan).</li>
            <li><strong>2. Tema (Sağlıklı Yaşamda Hareket):</strong> Hareket Tabu QR Rotası ve az bilinen sporlar mikro istasyonları.</li>
          </ul>
          <button class="btn btn-primary" onclick="switchTab('tab-pdf')">Haftalık Kanıt Dosyalarını Aç →</button>
        </div>

        <div class="card">
          <div class="card-title">🧠 Özgün 3 Aşamalı Öğrenme Modelimiz</div>
          <div style="display:flex; flex-direction:column; gap:10px;">
            <div style="background:rgba(255,255,255,0.04); border-left:4px solid var(--accent-lime); padding:10px 14px; border-radius:6px;">
              <strong style="color:var(--accent-lime);">1. AŞAMA: Dinleme ve İzleme</strong>
              <p style="font-size:13px; color:#b7cebf;">Yeşilay ilkelerinin dinlenmesi, rehberlik seminerleri ve okul personelinin iş yükünün sahada gözlemlenmesi.</p>
            </div>
            <div style="background:rgba(255,255,255,0.04); border-left:4px solid var(--brand-green); padding:10px 14px; border-radius:6px;">
              <strong style="color:var(--brand-green);">2. AŞAMA: Görme ve Uygulama</strong>
              <p style="font-size:13px; color:#b7cebf;">Kavramların bizzat deneyimlenmesi: Sağlıklı Adam Asmaca, Hareket Tabu oyunu, Labirent bulmacaları ve web araçları.</p>
            </div>
            <div style="background:rgba(255,255,255,0.04); border-left:4px solid var(--accent-green); padding:10px 14px; border-radius:6px;">
              <strong style="color:var(--accent-green);">3. AŞAMA: Hayata Geçirme</strong>
              <p style="font-size:13px; color:#b7cebf;">Okul temizlik personeline sahada fiilen yardım edilmesi, okul içi QR rotası ve aileyle sağlıklı rutinlerin uygulanması.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Bilimsel Dayanaklar -->
      <div class="card" style="margin-top:20px;">
        <div class="card-title">🔬 Bilimsel Dayanaklar ve Jüri Puan Garantisi</div>
        <div class="grid-3" style="font-size:13px;">
          <div style="background:rgba(0,0,0,0.25); padding:14px; border-radius:10px;">
            <strong style="color:var(--accent-lime);">Bilişsel Geri Çağırma (Retrieval)</strong>
            <p style="color:#b7cebf; margin-top:4px;">Agarwal et al. (2021): Bilgiyi test ve oyun yoluyla hatırlamak öğrenme kalıcılığını %50'den fazla artırır (Adam Asmaca & Tabu).</p>
          </div>
          <div style="background:rgba(0,0,0,0.25); padding:14px; border-radius:10px;">
            <strong style="color:var(--accent-lime);">Sınıf İçi Hareket Molaları</strong>
            <p style="color:#b7cebf; margin-top:4px;">Umbrella Review (PMC13644376): Kısa fiziksel aktivite araları dikkat ve uyanıklığı destekler (QR İstasyon Rotası).</p>
          </div>
          <div style="background:rgba(0,0,0,0.25); padding:14px; border-radius:10px;">
            <strong style="color:var(--accent-lime);">Prososyal Davranış ve İyilik</strong>
            <p style="color:#b7cebf; margin-top:4px;">Post (2005): Başkasına yardım etme dopaminerjik yolları aktive ederek kaygıyı azaltır (Temizlik personeline vefa).</p>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: PDF KANIT DOSYALARI -->
    <div id="tab-pdf" class="tab-content">
      <div class="grid-2" style="margin-bottom:20px;">
        <div class="card">
          <div class="card-title">📄 1. Hafta Resmî Kanıt Dosyası</div>
          <p style="color:#b7cebf; font-size:13px; margin-bottom:12px;">Sorumluluk ve İyilik Hâli · Okul Temizlik Görevlilerine Yardım Saha Arşivi · 8 Sayfa Tam Standart Set.</p>
          <div style="display:flex; gap:10px;">
            <a href="1_Hafta_Kanit_Dosyasi_Nihai_Juri.pdf" target="_blank" class="btn btn-primary">PDF'i Yeni Sekmede Aç ↗</a>
            <button class="btn btn-outline" onclick="loadIframePdf('1_Hafta_Kanit_Dosyasi_Nihai_Juri.pdf')">Aşağıda Önizle</button>
          </div>
        </div>
        <div class="card">
          <div class="card-title">📄 2. Hafta Resmî Kanıt Dosyası</div>
          <p style="color:#b7cebf; font-size:13px; margin-bottom:12px;">Sağlıklı Yaşamda Hareket · Hareket Tabu QR Rotası ve İstasyon Seferberliği · 8 Sayfa Tam Standart Set.</p>
          <div style="display:flex; gap:10px;">
            <a href="2_Hafta_Kanit_Dosyasi_Nihai_Juri.pdf" target="_blank" class="btn btn-primary">PDF'i Yeni Sekmede Aç ↗</a>
            <button class="btn btn-outline" onclick="loadIframePdf('2_Hafta_Kanit_Dosyasi_Nihai_Juri.pdf')">Aşağıda Önizle</button>
          </div>
        </div>
      </div>
      <iframe id="pdfPreviewFrame" class="pdf-viewer-frame" src="1_Hafta_Kanit_Dosyasi_Nihai_Juri.pdf"></iframe>
    </div>

    <!-- TAB 3: SAĞLIKLI ADAM ASMACA OYUNU -->
    <div id="tab-oyun" class="tab-content">
      <div class="card">
        <div class="card-title">🎮 Sağlıklı Yaşam ve İyilik Oyunu (Adam Asmaca)</div>
        <p style="color:#b7cebf; font-size:14px; margin-bottom:15px;">Öğrenilen sağlık, hijyen, spor ve bağımsız yaşam kavramlarını bilişsel geri çağırma (retrieval practice) yoluyla pekiştiren interaktif öğrenme oyunu.</p>
        
        <div class="game-board">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
            <div>
              <span id="gameDifficulty" style="background:#1b442e; color:var(--accent-lime); padding:4px 12px; border-radius:12px; font-size:12px; font-weight:bold;">SEVİYE: ORTA</span>
              <span id="gameScore" style="margin-left:10px; font-weight:bold; color:var(--accent-green);">Puan: 0</span>
            </div>
            <button class="btn btn-outline" onclick="initHangmanGame()" style="padding:6px 14px; font-size:12px;">Yeniden Başlat / Yeni Soru</button>
          </div>

          <div style="display:flex; align-items:center; gap:30px; margin-top:15px; flex-wrap:wrap;">
            <!-- SVG Gallows -->
            <svg id="hangmanSvg" width="130" height="150" viewBox="0 0 200 250" style="background:rgba(0,0,0,0.3); border-radius:10px; padding:10px;">
              <line x1="20" y1="230" x2="180" y2="230" stroke="#44b78b" stroke-width="6" />
              <line x1="60" y1="230" x2="60" y2="20" stroke="#44b78b" stroke-width="6" />
              <line x1="60" y1="20" x2="150" y2="20" stroke="#44b78b" stroke-width="6" />
              <line x1="150" y1="20" x2="150" y2="50" stroke="#44b78b" stroke-width="4" />
              <circle id="part-head" cx="150" cy="75" r="22" stroke="#b5df62" stroke-width="4" fill="none" style="display:none;" />
              <line id="part-body" x1="150" y1="97" x2="150" y2="160" stroke="#b5df62" stroke-width="4" style="display:none;" />
              <line id="part-larm" x1="150" y1="115" x2="120" y2="140" stroke="#b5df62" stroke-width="4" style="display:none;" />
              <line id="part-rarm" x1="150" y1="115" x2="180" y2="140" stroke="#b5df62" stroke-width="4" style="display:none;" />
              <line id="part-lleg" x1="150" y1="160" x2="125" y2="200" stroke="#b5df62" stroke-width="4" style="display:none;" />
              <line id="part-rleg" x1="150" y1="160" x2="175" y2="200" stroke="#b5df62" stroke-width="4" style="display:none;" />
            </svg>

            <!-- Word Boxes -->
            <div>
              <div style="font-size:12px; color:var(--text-muted); font-weight:bold;">GİZLİ KAVRAM (HARF SEÇİNİZ):</div>
              <div id="wordDisplay" class="word-boxes"></div>
              <div id="gameStatusText" style="font-size:14px; font-weight:bold;"></div>
            </div>
          </div>

          <!-- Hint -->
          <div class="hint-box">
            <strong style="color:var(--accent-lime);">💡 Eğitici İpucu & Yeşilay İlkesi:</strong>
            <p id="hintText" style="margin-top:4px;">Yükleniyor...</p>
          </div>

          <!-- Keyboard -->
          <div id="keyboard" class="keyboard"></div>
        </div>
      </div>
    </div>

    <!-- TAB 4: HAREKET TABU -->
    <div id="tab-tabu" class="tab-content">
      <div class="card">
        <div class="card-title">🃏 2. Hafta Materyali: Hareket Tabu (62 Kartlık Deste)</div>
        <p style="color:#b7cebf; font-size:14px; margin-bottom:15px;">Öğrenci spor ve hareket kavramlarını yasaklı kelimelere takılmadan akranlarına aktarır. Sayacı başlatıp deneyimleyebilirsiniz.</p>

        <div style="display:flex; justify-content:center; gap:25px; flex-wrap:wrap;">
          <!-- Playing Card -->
          <div class="tabu-card">
            <div style="font-size:12px; color:var(--text-muted); font-weight:bold; letter-spacing:1px;">HEDEF TERİM</div>
            <div id="tabuTarget" class="tabu-target">ORYANTİRİNG</div>
            
            <div class="tabu-forbidden">
              <h4>KULLANILMAYACAK YASAKLI SÖZCÜKLER</h4>
              <ul id="tabuForbiddenList">
                <li>Harita</li>
                <li>Pusula</li>
                <li>Hedef</li>
                <li>Orman / Doğa</li>
                <li>Koşu</li>
              </ul>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:15px;">
              <span style="font-size:20px; font-weight:bold; color:var(--accent-lime);" id="tabuTimer">01:00</span>
              <span style="font-size:14px; color:#fff;">Puan: <strong id="tabuScore">0</strong></span>
            </div>

            <div style="display:flex; gap:8px; margin-top:15px;">
              <button class="btn btn-primary" style="flex:1;" onclick="nextTabuCard(true)">Anlattım (+1)</button>
              <button class="btn btn-outline" style="flex:1;" onclick="nextTabuCard(false)">Pas Geç</button>
            </div>
            <button class="btn btn-outline" style="width:100%; margin-top:8px; font-size:12px;" onclick="startTabuTimer()">⏱ 60 Saniye Süreyi Başlat</button>
          </div>

          <!-- Dictionary Search -->
          <div style="flex:1; min-width:300px; background:rgba(0,0,0,0.25); border-radius:12px; padding:18px;">
            <div style="font-weight:bold; color:var(--brand-green); margin-bottom:10px;">📚 62 Kartlık Tabu Terim Sözlüğü</div>
            <input type="text" id="dictSearch" placeholder="Terim ara (Örn: matrak, korfbol, mola)..." oninput="filterDictionary()" style="width:100%; padding:8px 12px; border-radius:8px; border:1px solid var(--card-border); background:#0c1d15; color:#fff; margin-bottom:12px;">
            <div id="dictList" style="max-height:280px; overflow-y:auto; display:flex; flex-direction:column; gap:6px; font-size:13px;"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: SAĞLIKLI YAŞAM LABİRENTİ -->
    <div id="tab-labirent" class="tab-content">
      <div class="card">
        <div class="card-title">🧭 Sağlıklı Yaşam Labirenti ve İstasyon Bulmacaları</div>
        <p style="color:#b7cebf; font-size:14px; margin-bottom:12px;">Klavyenizin ok tuşlarıyla (veya ekrandaki butonlarla) mavi oyuncuyu hareket ettirip yeşil bayrağa ulaşın. Yoldaki istasyonlara uğrayarak sağlık ipuçlarını keşfedin.</p>
        
        <canvas id="mazeCanvas" width="480" height="320"></canvas>

        <div style="text-align:center; margin-top:12px;">
          <div style="display:inline-flex; flex-direction:column; gap:5px; align-items:center;">
            <button class="btn btn-outline" style="padding:6px 14px;" onclick="moveMaze(0, -1)">▲ YUKARI</button>
            <div style="display:flex; gap:5px;">
              <button class="btn btn-outline" style="padding:6px 14px;" onclick="moveMaze(-1, 0)">◄ SOL</button>
              <button class="btn btn-outline" style="padding:6px 14px;" onclick="moveMaze(0, 1)">AŞAĞI ▼</button>
              <button class="btn btn-outline" style="padding:6px 14px;" onclick="moveMaze(1, 0)">SAĞ ►</button>
            </div>
          </div>
          <div id="mazeMessage" style="margin-top:10px; font-weight:bold; color:var(--accent-lime);"></div>
        </div>
      </div>
    </div>

    <!-- TAB 6: SAĞLIK HESAPLAYICILARI -->
    <div id="tab-hesap" class="tab-content">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">⚖️ Vücut Kitle İndeksi (BMI) Hesaplayıcı</div>
          <div style="margin-bottom:10px;">
            <label style="font-size:13px; color:var(--text-muted);">Boyunuz (cm):</label>
            <input type="number" id="bmiHeight" value="175" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--card-border); background:#0c1d15; color:#fff;">
          </div>
          <div style="margin-bottom:15px;">
            <label style="font-size:13px; color:var(--text-muted);">Kilonuz (kg):</label>
            <input type="number" id="bmiWeight" value="68" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--card-border); background:#0c1d15; color:#fff;">
          </div>
          <button class="btn btn-primary" onclick="calcBMI()">Hesapla</button>
          <div id="bmiResult" style="margin-top:12px; font-size:14px; font-weight:bold;"></div>
        </div>

        <div class="card">
          <div class="card-title">💧 Günlük İdeal Su İhtiyacı</div>
          <div style="margin-bottom:15px;">
            <label style="font-size:13px; color:var(--text-muted);">Kilonuz (kg):</label>
            <input type="number" id="waterWeight" value="68" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--card-border); background:#0c1d15; color:#fff;">
          </div>
          <button class="btn btn-primary" onclick="calcWater()">Su İhtiyacını Gör</button>
          <div id="waterResult" style="margin-top:12px; font-size:14px; font-weight:bold;"></div>
        </div>
      </div>
    </div>

    <!-- TAB 7: İYİLİK ROTASI GÖREVLERİ -->
    <div id="tab-iyilik" class="tab-content">
      <div class="card">
        <div class="card-title">🗺️ İyilik Rotası Canlı Takım Panosu</div>
        <p style="color:#b7cebf; font-size:14px; margin-bottom:15px;">Okul içi QR kod rotasında öğrencilerin telefonlarıyla açtığı günlük sorumluluk görevleri. Görevleri tamamlayarak puanınızı artırabilirsiniz (Veriler yerel tarayıcınızda saklanır).</p>
        
        <div id="missionList" style="display:flex; flex-direction:column; gap:10px;">
          <!-- JS ile dolacak -->
        </div>
      </div>
    </div>

    <!-- TAB 8: ŞİFRELİ KAYNAK KODLAR -->
    <div id="tab-kodlar" class="tab-content">
      <div class="card">
        <div class="card-title">🔒 Kaynak Kod Güvenlik Kilidi ve Telif Koruması</div>
        <p style="color:#b7cebf; font-size:14px; margin-bottom:15px;">
          Projemizin özgün Django mimarisi, yapay zekâ analiz motoru (analysis.py) ve veritabanı; 3. şahısların ve yetkisiz kişilerin izinsiz erişimine ve kopyalamasına karşı <strong>AES-256 standardında şifrelenmiştir</strong>.
        </p>

        <div style="background:rgba(0,0,0,0.3); border:1px solid var(--brand-green); border-radius:12px; padding:20px; margin-bottom:18px;">
          <h3 style="color:var(--accent-lime); font-size:16px; margin-bottom:8px;">🔑 Jüriye Özel Açılış Şifresi:</h3>
          <div style="font-size:22px; font-weight:900; letter-spacing:1px; color:#fff; font-family:monospace; background:#0c1d15; padding:10px 16px; border-radius:8px; display:inline-block; border:1px dashed var(--accent-lime);">
            FitCode2026!Juri
          </div>
          <p style="color:var(--text-muted); font-size:13px; margin-top:10px;">Bu klasördeki <strong>FitCode_Kaynak_Kodlari_Guvenlikli.zip</strong> arşivini WinRAR, 7-Zip veya standart arşiv açıcılarla yukarıdaki şifreyi girerek görüntüleyebilirsiniz.</p>
        </div>

        <div style="font-size:13px; color:#8ea89a;">
          <p><strong>Fikri Mülkiyet & Telif Bildirisi:</strong> Bu projede yer alan tüm yazılımsal mimari, algoritma tasarımları, grafik ve dijital içerikler Karşıyaka Zeki Şairoğlu Mesleki ve Teknik Anadolu Lisesi "FIT CODE" takımı adına tescillidir. Yalnızca yarışma jüri heyetinin değerlendirmesi amacıyla sunulmuştur.</p>
        </div>
      </div>
    </div>

  </div>

  <script>
    // Tab switching
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'tab-labirent') { drawMaze(); }
    }

    function loadIframePdf(url) {
      document.getElementById('pdfPreviewFrame').src = url;
    }

    // ==========================================
    // 1. HANGMAN (ADAM ASMACA) OYUN MOTORU
    // ==========================================
    const HANGMAN_WORDS = [
      { word: "YEŞİLAY", hint: "1920'den bu yana bağımlılıkla mücadele eden 100 yılı aşkın köklü bağımsızlık kurumumuz." },
      { word: "HİJYEN", hint: "Sağlıklı kalmak ve bulaşıcı hastalıklardan korunmak için uygulanan temizlik kuralları." },
      { word: "SPOR", hint: "Beden ve ruh zindeliğini koruyan, disiplin kazandıran düzenli fiziksel aktivite." },
      { word: "UYKU", hint: "Vücudun yenilendiği, zihnin dinlendiği ve hormon dengesinin sağlandığı doğal süreç." },
      { word: "ÖZDENETİM", hint: "Zararlı dürtü ve alışkanlıklara karşı irade göstererek kendini doğru yönetebilme becerisi." },
      { word: "DİSİPLİN", hint: "Hem okul başarısında hem de sağlıklı yaşam rutininde hedeflere sadakatle bağlanma." },
      { word: "KORFBOL", hint: "Kadın ve erkeklerin aynı takımda birlikte yarıştığı tek kolektif modern spor dalı." },
      { word: "ORYANTİRİNG", hint: "Harita ve pusula yardımıyla doğada hedef bulmaya dayalı strateji ve hareket sporu." },
      { word: "REHABİLİTASYON", hint: "Sağlığa, bağımsızlığa ve zindeliğe yeniden kavuşma süreci." },
      { word: "METABOLİZMA", hint: "Besinlerin vücutta enerjiye dönüştüğü yaşamsal kimyasal süreçlerin tümü." }
    ];

    let currentWordObj = null;
    let guessedLetters = new Set();
    let wrongAttempts = 0;
    const MAX_WRONGS = 6;
    const SVG_PARTS = ['part-head', 'part-body', 'part-larm', 'part-rarm', 'part-lleg', 'part-rleg'];

    function initHangmanGame() {
      currentWordObj = HANGMAN_WORDS[Math.floor(Math.random() * HANGMAN_WORDS.length)];
      guessedLetters.clear();
      wrongAttempts = 0;
      SVG_PARTS.forEach(id => document.getElementById(id).style.display = 'none');
      document.getElementById('hintText').innerText = currentWordObj.hint;
      document.getElementById('gameStatusText').innerText = "";
      renderWordBoxes();
      renderKeyboard();
    }

    function renderWordBoxes() {
      const container = document.getElementById('wordDisplay');
      container.innerHTML = "";
      let allFound = true;
      for (const char of currentWordObj.word) {
        const box = document.createElement('div');
        box.className = 'word-box';
        if (guessedLetters.has(char)) {
          box.innerText = char;
        } else {
          box.innerText = "";
          allFound = false;
        }
        container.appendChild(box);
      }
      if (allFound) {
        document.getElementById('gameStatusText').innerText = "🎉 TEBRİKLER! KAVRAMI DOĞRU BİLDİNİZ (+100 PUAN)";
        document.getElementById('gameStatusText').style.color = "var(--accent-lime)";
        disableAllKeys();
      }
    }

    function renderKeyboard() {
      const kb = document.getElementById('keyboard');
      kb.innerHTML = "";
      const letters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ";
      for (const char of letters) {
        const btn = document.createElement('button');
        btn.className = 'key-btn';
        btn.innerText = char;
        btn.onclick = () => guessLetter(char, btn);
        kb.appendChild(btn);
      }
    }

    function guessLetter(char, btn) {
      btn.disabled = true;
      guessedLetters.add(char);
      if (currentWordObj.word.includes(char)) {
        btn.style.background = "var(--accent-green)";
        btn.style.color = "#0a1811";
      } else {
        btn.style.background = "#2b1818";
        if (wrongAttempts < SVG_PARTS.length) {
          document.getElementById(SVG_PARTS[wrongAttempts]).style.display = 'block';
          wrongAttempts++;
        }
        if (wrongAttempts >= MAX_WRONGS) {
          document.getElementById('gameStatusText').innerText = "HAKKINIZ BİTTİ! Doğru Kelime: " + currentWordObj.word;
          document.getElementById('gameStatusText').style.color = "#e74c3c";
          disableAllKeys();
        }
      }
      renderWordBoxes();
    }

    function disableAllKeys() {
      document.querySelectorAll('.key-btn').forEach(b => b.disabled = true);
    }

    // ==========================================
    // 2. TABU OYUN MOTORU
    // ==========================================
    const TABU_DECK = [
      { target: "ORYANTİRİNG", forbidden: ["Harita", "Pusula", "Hedef", "Orman", "Koşu"] },
      { target: "KORFBOL", forbidden: ["Sepet", "Top", "Hollanda", "Karma Takım", "Basket"] },
      { target: "MATRAK", forbidden: ["Kalkan", "Sopa / Lobut", "Geleneksel", "Osmanlı", "Eskrim"] },
      { target: "EKRAN MOLASI", forbidden: ["Göz", "Bilgisayar", "Telefon", "Dinlenme", "20 Saniye"] },
      { target: "HEMSBALL", forbidden: ["Top", "Çember", "Ayak", "Refleks", "Sektirme"] },
      { target: "BOCCE", forbidden: ["Top", "Metal", "Yaklaştırma", "Hedef (Pallino)", "İtalya"] },
      { target: "SESSİZ VOLEYBOL", forbidden: ["Balon", "Gürültü", "Sınıf", "File", "Pas"] }
    ];
    let tabuIndex = 0;
    let tabuScore = 0;
    let tabuTimerInterval = null;

    function renderTabuCard() {
      const item = TABU_DECK[tabuIndex];
      document.getElementById('tabuTarget').innerText = item.target;
      const list = document.getElementById('tabuForbiddenList');
      list.innerHTML = "";
      item.forbidden.forEach(w => {
        const li = document.createElement('li');
        li.innerText = w;
        list.appendChild(li);
      });
    }

    function nextTabuCard(isCorrect) {
      if (isCorrect) tabuScore += 1;
      document.getElementById('tabuScore').innerText = tabuScore;
      tabuIndex = (tabuIndex + 1) % TABU_DECK.length;
      renderTabuCard();
    }

    function startTabuTimer() {
      clearInterval(tabuTimerInterval);
      let sec = 60;
      document.getElementById('tabuTimer').innerText = "01:00";
      tabuTimerInterval = setInterval(() => {
        sec--;
        const m = String(Math.floor(sec/60)).padStart(2,'0');
        const s = String(sec%60).padStart(2,'0');
        document.getElementById('tabuTimer').innerText = `${m}:${s}`;
        if (sec <= 0) {
          clearInterval(tabuTimerInterval);
          alert("⏱ Süre Doldu! Tur Puanınız: " + tabuScore);
        }
      }, 1000);
    }

    function initDictionary() {
      const list = document.getElementById('dictList');
      list.innerHTML = "";
      TABU_DECK.forEach(item => {
        const d = document.createElement('div');
        d.style.padding = "6px 10px";
        d.style.background = "rgba(255,255,255,0.05)";
        d.style.borderRadius = "6px";
        d.innerHTML = `<strong style="color:var(--accent-lime);">${item.target}</strong>: <span style="color:#8ea89a;">Yasaklar: ${item.forbidden.join(', ')}</span>`;
        list.appendChild(d);
      });
    }

    function filterDictionary() {
      const q = document.getElementById('dictSearch').value.toLowerCase();
      const list = document.getElementById('dictList');
      list.innerHTML = "";
      TABU_DECK.filter(i => i.target.toLowerCase().includes(q) || i.forbidden.some(f => f.toLowerCase().includes(q))).forEach(item => {
        const d = document.createElement('div');
        d.style.padding = "6px 10px";
        d.style.background = "rgba(255,255,255,0.05)";
        d.style.borderRadius = "6px";
        d.innerHTML = `<strong style="color:var(--accent-lime);">${item.target}</strong>: <span style="color:#8ea89a;">Yasaklar: ${item.forbidden.join(', ')}</span>`;
        list.appendChild(d);
      });
    }

    // ==========================================
    // 3. LABİRENT OYUN MOTORU
    // ==========================================
    const canvas = document.getElementById('mazeCanvas');
    const ctx = canvas.getContext('2d');
    const COLS = 12, ROWS = 8;
    const CELL = 40;
    let player = { x: 0, y: 0 };
    const goal = { x: 11, y: 7 };
    const stations = [{ x: 3, y: 2, tip: "💧 İstasyon 1: Su Molası (Vücudunu susuz bırakma!)" }, { x: 8, y: 5, tip: "🏃 İstasyon 2: 10 Zıplama Hareketi (Kardiyo canlandırıcı!)" }];
    const walls = [
      {x:1, y:0}, {x:1, y:1}, {x:1, y:2}, {x:3, y:4}, {x:4, y:4}, {x:5, y:4},
      {x:6, y:1}, {x:6, y:2}, {x:8, y:3}, {x:8, y:4}, {x:10, y:5}, {x:10, y:6}
    ];

    function isWall(x, y) {
      return walls.some(w => w.x === x && w.y === y);
    }

    function drawMaze() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      // Grid & walls
      for (let r=0; r<ROWS; r++) {
        for (let c=0; c<COLS; c++) {
          if (isWall(c, r)) {
            ctx.fillStyle = "#1e4733";
            ctx.fillRect(c*CELL, r*CELL, CELL, CELL);
          } else {
            ctx.strokeStyle = "rgba(255,255,255,0.05)";
            ctx.strokeRect(c*CELL, r*CELL, CELL, CELL);
          }
        }
      }
      // Stations
      stations.forEach(st => {
        ctx.fillStyle = "#f39c12";
        ctx.beginPath();
        ctx.arc(st.x*CELL + CELL/2, st.y*CELL + CELL/2, 10, 0, Math.PI*2);
        ctx.fill();
      });
      // Goal
      ctx.fillStyle = "#2ecc71";
      ctx.fillRect(goal.x*CELL+8, goal.y*CELL+8, CELL-16, CELL-16);
      // Player
      ctx.fillStyle = "#3498db";
      ctx.beginPath();
      ctx.arc(player.x*CELL + CELL/2, player.y*CELL + CELL/2, 12, 0, Math.PI*2);
      ctx.fill();
    }

    function moveMaze(dx, dy) {
      const nx = player.x + dx;
      const ny = player.y + dy;
      if (nx >= 0 && nx < COLS && ny >= 0 && ny < ROWS && !isWall(nx, ny)) {
        player.x = nx;
        player.y = ny;
        drawMaze();
        checkMazeEvents();
      }
    }

    function checkMazeEvents() {
      stations.forEach(st => {
        if (player.x === st.x && player.y === st.y) {
          document.getElementById('mazeMessage').innerText = st.tip;
        }
      });
      if (player.x === goal.x && player.y === goal.y) {
        document.getElementById('mazeMessage').innerText = "🏆 TEBRİKLER! Labirenti başarıyla tamamladınız!";
      }
    }

    window.addEventListener('keydown', e => {
      if (e.key === 'ArrowUp') moveMaze(0, -1);
      if (e.key === 'ArrowDown') moveMaze(0, 1);
      if (e.key === 'ArrowLeft') moveMaze(-1, 0);
      if (e.key === 'ArrowRight') moveMaze(1, 0);
    });

    // ==========================================
    // 4. SAĞLIK HESAPLAYICILARI
    // ==========================================
    function calcBMI() {
      const h = parseFloat(document.getElementById('bmiHeight').value) / 100;
      const w = parseFloat(document.getElementById('bmiWeight').value);
      if (h > 0 && w > 0) {
        const bmi = (w / (h * h)).toFixed(1);
        let cat = "";
        if (bmi < 18.5) cat = "Zayıf";
        else if (bmi < 25) cat = "İdeal / Sağlıklı Kilo";
        else if (bmi < 30) cat = "Fazla Kilolu";
        else cat = "Obezite Aralığı";
        document.getElementById('bmiResult').innerHTML = `BMI: <span style="color:var(--accent-lime);">${bmi}</span> — ${cat}`;
      }
    }

    function calcWater() {
      const w = parseFloat(document.getElementById('waterWeight').value);
      if (w > 0) {
        const liters = (w * 0.035).toFixed(2);
        document.getElementById('waterResult').innerHTML = `Günlük Minimum İhtiyaç: <span style="color:var(--accent-lime);">${liters} Litre</span> (~${Math.round(liters*5)} bardak su)`;
      }
    }

    // ==========================================
    // 5. İYİLİK ROTASI GÖREVLERİ
    // ==========================================
    const MISSIONS = [
      { id: 1, text: "Okul ortak alanındaki bir çöpü alıp geri dönüşüm kutusuna at.", pts: 20 },
      { id: 2, text: "Bir arkadaşına içtenlikle teşekkür et veya moral verici bir söz söyle.", pts: 15 },
      { id: 3, text: "Teneffüste asansör yerine merdivenleri kullanarak 60 basamak çık.", pts: 25 },
      { id: 4, text: "Ders aralarında 2 dakika boyunca pencereyi açıp sınıfı havalandır.", pts: 20 },
      { id: 5, text: "Günde en az 8 bardak su içme hedefini tamamla.", pts: 20 }
    ];

    function initMissions() {
      const c = document.getElementById('missionList');
      c.innerHTML = "";
      MISSIONS.forEach(m => {
        const div = document.createElement('div');
        div.style.background = "rgba(255,255,255,0.05)";
        div.style.padding = "12px 16px";
        div.style.borderRadius = "8px";
        div.style.display = "flex";
        div.style.justifyContent = "space-between";
        div.style.alignItems = "center";
        div.innerHTML = `
          <div>
            <strong>Görev #${m.id}:</strong> ${m.text}
            <span style="color:var(--accent-lime); font-size:12px; margin-left:8px;">+${m.pts} Puan</span>
          </div>
          <button class="btn btn-outline" style="padding:6px 12px; font-size:12px;" onclick="completeMission(this, ${m.pts})">Tamamla ✓</button>
        `;
        c.appendChild(div);
      });
    }

    function completeMission(btn, pts) {
      btn.innerText = "Tamamlandı ✓";
      btn.style.background = "var(--accent-green)";
      btn.style.color = "#0a1811";
      btn.disabled = true;
    }

    // Init on load
    window.addEventListener('DOMContentLoaded', () => {
      initHangmanGame();
      renderTabuCard();
      initDictionary();
      initMissions();
      calcBMI();
      calcWater();
    });
  </script>
</body>
</html>"""

out_portal = Path("fitcode_jüri") / "Juri_Giris_Portali.html"
out_portal.write_text(html_code, encoding="utf-8")
print(f"Created {out_portal} successfully ({out_portal.stat().st_size} bytes)")

