# translate_english_subtitle

## 簡介 Description
Demo link: https://youtu.be/MAchR7DgmL0

Press keyboard to capture the word. Use web crawler to search for the word and show with a clean interface. Users can save their words into excel.

執行程式後按下鍵盤特定鍵開啟擷取功能，此時能將要搜尋的單字用滑鼠框起來，確認該單字後程式便會使用爬蟲搜尋該單字，並使用GUI頁面進行顯示。可將搜尋到的單字紀錄到excel中方便日後進行複習。

## 使用套件
- 偵測滑鼠位置及背景的鍵盤事件(pynput模組)
- 螢幕截圖(pyautogui模組)
- 辨識文字功能(pytesseract模組)
- 爬蟲(requests, bs4, re等模組)
- 彈出視窗(PySimpleGUI模組)
- 將資料寫入excel (openpyxl模組)

## 程式流程圖
<img src="https://user-images.githubusercontent.com/60069744/145408175-edaa905a-fe74-4dc1-bba8-90234d862895.png" width="500">

## 成果展示
- 確認畫面
<img src="https://user-images.githubusercontent.com/60069744/145408434-cdf474e8-dae8-4ea6-8add-7617eb9f099a.png" width="250">

- 顯示查詢結果畫面
<img src="https://user-images.githubusercontent.com/60069744/145408612-21e0fe60-a86a-49df-a07a-8cb159172231.png" width="300">

- 查無資料畫面
<img src="https://user-images.githubusercontent.com/60069744/145408715-567c02ff-0763-4d73-903e-1e9c66168bbb.png" width="100">

- 儲存至 excel
<img src="https://user-images.githubusercontent.com/60069744/145408904-0e46a5f7-b0ae-4439-b664-e9d1a1d7aa15.png" height="200">
