# Braille Music Editor Add-On for NVDA
* 作者: Gianluca Casalino
* 下載連結: https://github.com/GianGythub/bme2Nvda/raw/master/packages/bme2-2020.12.1.nvda-addon 

此專案是專供 Braille Music Editor 2 (Bme2) 軟體使用的 appModule，並且由 Jaws For Windows 的 Bme2 附加元件的原作者設計。
**請注意：** 此附加元件是由 Gianluca Casalino 免費提供，無論作者或任何貢獻者都沒有參與 Bme2 軟體的銷售或開發。如果你在使用或安裝方面碰到任何問題，請聯繫作者，或透過 Github 專案的 "Issues" 功能來回報問題。

### [官方 Github 儲存庫](https://github.com/GianGythub/bme2Nvda/)

## 附加元件的功能

### 對語音報讀的支援：

* 對話窗與選單可正確報讀。
* 使用 BME2 引擎來支援音樂元素的自然語音。
* 實作了逐字元、逐字、逐段落、逐行報讀，以及從游標所在位置報讀、報讀至游標所在位置，以及報讀全部。
* 當某個區塊內容被選取時自動報讀。
* 當輸入焦點透過 Windows 標準操作方式切換至文字編輯器時自動報讀。
* 有些特殊的對話窗，例如 play midi、part selector、和 instruments midi seledctor 視窗，現在可以正確報讀，而且當游標四處移動或者在文字方塊中輸入文字與選取文字時，也都可以正確報讀。
* 使用 BME2 文字處理器來處理打字回應，以便讓音樂元素能夠正確報讀。

### 對點字顯示器的支援：

* 對話窗與選單可正確顯示。
* 編輯器的內容可以在點顯器上正確顯示，而且使用者可以透過點顯器的捲動按鈕或游標移動按鈕來移動。
* 選取內容會使用第 7 點和第 8 點來加以標示，而且在使用標準 Windows 操作來改變選取範圍時（例如 Shift+方向鍵），也會跟著更新。

### 對鍵盤的支援：

* **NVDA+Alt+上方向鍵**：從開頭報讀至游標所在位置。
* **NVDA+Alt+下方向鍵**：從游標所在位置報讀至結尾。
* **NVDA+o**：如果游標所在位置的音樂元素有相關屬性，就把它們報讀出來。
* **F12**: 如果游標所在位置有歌詞，就把它們報讀出來。

## 已知問題：

* Nvda Review Cursor（滑鼠游標）功能尚未於 BME2 中實作.
* 在音符上面執行 braille routing 時，midi 事件不會觸發。此問題需要進一步研究。
* 在執行報讀全部的命令時，如果文字內容特別長，NVDA 會當掉。

## 修改紀錄

底下是此附加元件各版本的修改紀錄。如果版本編號後面有括弧包住的文字，那些文字是開發狀態。目前開發中的版本不會包含在內，因為在它被標示為穩定或放棄之前，都可能持續變動。

### Version 2020.12.1

* added support for the demo version of Bme2

### Version 2020.04.4

* Completely reengenired the old release of add-on. It is now compatible with 2019.3 release of Nvda and following.
* Added support for all special dialog windows as for example parts selector or midi instruments selector.
* Added some new commands script.

## 致謝

特別感謝 Alberto Buffolino，他很有耐心的讓我了解 NVDA 程式碼這幾年以來有哪些變動。
