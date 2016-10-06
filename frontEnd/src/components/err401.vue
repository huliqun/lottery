<template>
  <h1 class="title">
    <span class="cn" id="title-cn">授权失败</span>
    <span class="en" id="title-en">Bad Request</span>
    <span class="de" id="title-de">Fehlerhafte Anfrage</span>
    <span class="hu" id="title-hu">Hibás lekérdezés</span>
    <span class="ru" id="title-ru">Неверный запрос</span>
  </h1>
  <div class="errorBody">
    <div class="errorBox">
      <div class="errorData">
        <div class="statusCode">401</div>
        <div class="statusText">
          <span class="cn">交易未授权或者会话失效</span>
          <span class="en">Your Browser sent a Bad Request</span>
          <span class="de">Ihr Browser hat eine fehlerhafte Anfrage geschickt</span>
          <span class="hu">A böngészője hibás lekérdezést küldött</span>
          <span class="ru">Ваш браузер послал неверный запрос</span>
        </div>
      </div>
      <div class="errorDescription">
        <div class="description">
          <span class="cn">
            授权错误 <strong>不能处理</strong>. 请按下列步骤解决问题.
          </span>
          <span class="en">
            Your browser sent a request our server <strong>couldn't process</strong>. Please try again or follow the steps below to resolve this issue.
          </span>
          <span class="de">
            Ihr Browser hat eine Anfrage geschickt die unser Server <strong>nicht verarbeiten konnte</strong>. Bitte versuchen sie diese Schritte um den Fehler zu beheben.
          </span>
          <span class="hu">
            A böngészője olyan lekérdezést küldött, amit a szerverünk <strong>nem tudott feldolgozni</strong>. Kérjük, kövesse az alábbi lépéseket a probléma megoldása érdekében.
          </span>
          <span class="ru">
            Ваш браузер послал запрос, который наш сервер не в состоянии обработать. Пожалуйста, попытайтесь снова или следуйте инструкциям ниже для решения проблемы
          </span>
        </div>
        <div class="tips todo">
          <h2>
            <span class="cn">请按照下列步骤处理:</span>
            <span class="en">Please follow these steps to get back on track:</span>
            <span class="de">Bitte versuchen sie folgendes:</span>
            <span class="hu">Próbálja meg az alábbiakat:</span>
            <span class="ru">Пожалуйста, следуйте данным указаниям для возвращения в обычный режим:</span>
          </h2>
          <ul>
            <li>
              <span class="cn">
                检查<strong>更新</strong> 你的浏览器,推荐使用Chrome 或者 FireFox.
              </span>
              <span class="en">
                Check for any <strong>updates</strong> for your browser.
              </span>
              <span class="de">
                Laden sie eine <strong>neuere Version</strong> ihres Browsers runter.
              </span>
              <span class="hu">
                <strong>Frissítse a böngészőjét</strong> a legfrissebb verzióra.
              </span>
              <span class="ru">
                Проверьте для <strong>обновлений Вашего браузера</strong>.
              </span>
            </li>
            <li>
              <span class="cn">返回 <a href="/">首页</a> 并再次尝试.</span>
              <span class="en">Go to our <a href="/">Homepage</a> and try again from there.</span>
              <span class="de">Gehen sie zu unserer <a href="/">Homepage</a> und versuchen sie es von da erneut.</span>
              <span class="hu">Térjen vissza a <a href="/">kezdőlapra</a> és próbálja újra onnan.</span>
              <span class="ru">Вернитесь на <a href="/">домашнюю страницу</a> и попытайтесь снова.</span>
            </li>
            <li>
              <span class="cn">
                请联系系统管理人员,电话:400-400-4012.
              </span>
              <span class="en">
                If you typed the address for this site, check that you typed everything correctly.
              </span>
              <span class="de">
                Wenn sie die Addresse eingetippt haben, kontrollieren sie diese auf Tippfehler.
              </span>
              <span class="hu">
                Ha a címet kézzel adta be, ellenőrizze ezt gépelési hibákra.
              </span>
              <span class="ru">
                При наборе адреса этого сайта, проверьте корректность набора
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
</script>
<style>
* {
  margin: 0;
  padding: 0;
  -webkit-box-sizing: initial;
}

html, body {
  min-height: 100%;
}

body {
  position:relative;
  font-size: 11px;
  font-family: Verdana, sans-serif;
  background: #0a2b4f; /* Old browsers */
  background: -moz-linear-gradient(top, #0a2b4f 0%, #539ab8 100%); /* FF3.6+ */
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#0a2b4f), color-stop(100%,#539ab8)); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(top, #0a2b4f 0%,#539ab8 100%); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(top, #0a2b4f 0%,#539ab8 100%); /* Opera 11.10+ */
  background: -ms-linear-gradient(top, #0a2b4f 0%,#539ab8 100%); /* IE10+ */
  background: linear-gradient(to bottom, #0a2b4f 0%,#539ab8 100%); /* W3C */
}

a {
  color:#333;
}

.errorBody {
  min-height:780px;
  padding-top: 120px;
}

.errorBox {
  color: #333;
  position: relative;

  margin-left:auto;
  margin-right:auto;

  width: 880px;
  height: 300px;
  padding: 40px;

  background-color: rgba(255, 255, 255, 0.9);

  border-radius: 15px;
  box-shadow: 3px 3px 10px #333;
}

.statusCode,
.statusText {
  width: 320px;
  text-align: center;
  color: #555;
}

.statusCode {
  margin-top: 40px;
  font-size: 148px;
  font-weight: bold;
}

.statusText {
  font-size: 24px;
}

.errorDescription {
  position: absolute;
  top: 40px;
  right: 40px;
  width: 490px;
  height: 300px;
  padding-left:30px;
  border-left: 1px solid #e0e0e0;
}

.todo {
  position:absolute;
  bottom:0;
  width:490px;
}

@media (max-width: 980px) {
  .errorBody {
    padding-top:0;
  }

  .errorBox {
    width:auto;
    height:auto;
    margin:10px;
  }

  .statusCode {
    margin-top: 0;
  }

  .statusCode,
  .statusText {
    width:auto;
    text-align:center;
  }

  .errorDescription {
    position:relative;
    top:inherit;
    right:inherit;
    width:auto;
    height:auto;
    padding-left:0;
    border-left:0;
  }

  .todo {
    position:relative;
    width:auto;
    bottom:inherit;
  }

  .description {
    margin-top:16px;
    height:auto !important;
  }

  h2 {
    margin-top:16px;
  }
}

@media (max-width: 430px) {
  .statusCode {
    font-size:72px;
  }
}


.description {
  line-height:16px;
  height:100px;
}

h1.title {
  display:none;
}

h2 {
  font-size:11px;
  margin-bottom:20px;
}

.links ul li {
  float:left;
  line-height:27px;
  margin-right:20px;
  margin-bottom:-1px;
  height:27px;
  width:220px;
  border-top:1px solid #b3c6cc;;
  border-bottom:1px solid #b3c6cc;;
  list-style-type:none;
}

.links ul li:before{
  content: "\00BB\00A0";
}

.links ul li a {
  text-decoration:none;
  color:#333;
}

.links ul li a:hover {
  text-decoration:underline;
}

.tips ul li {
  line-height:27px;
  margin-right:20px;
  margin-bottom:-1px;
  border-top:1px solid #b3c6cc;;
  border-bottom:1px solid #b3c6cc;;
  list-style-type:none;
}

.tips ul li:before{
  content: "\00BB\00A0";
}

.en, .de, .hu, .ru {
  display:none;
}

#locale-flags {
  display:none;
  position:absolute;
  top:10px;
  right:10px;
}

.locale-cn .cn {
  display:inline;
}
.locale-cn .en,
.locale-cn .de,
.locale-cn .hu,
.locale-cn .ru {
  display:none;
}

.locale-en .en {
  display:inline;
}
.locale-en .cn,
.locale-en .de,
.locale-en .hu,
.locale-en .ru {
  display:none;
}

.locale-de .de {
  display:inline;
}
.locale-de .cn,
.locale-de .en,
.locale-de .hu,
.locale-de .ru {
  display:none;
}

.locale-hu .hu {
  display:inline;
}
.locale-hu .cn,
.locale-hu .en,
.locale-hu .de,
.locale-hu .ru{
  display:none;
}

.locale-ru .ru {
  display:inline;
}
.locale-ru .cn,
.locale-ru .de,
.locale-ru .hu,
.locale-ru .en {
  display:none;
}
</style>
