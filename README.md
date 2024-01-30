# Image Watermarking App

Python project that allows user to edit an image in order to add a custom watermark and save the edited file. It uses Tkinter and Pillow libraries to create a GUI and implement all the features.

## Getting Started
1. Clone the repository
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>git clone https://github.com/tarintrader/Watermarking-App.git
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="git clone https://github.com/Veluthil/Typing-Speed-Test-App.git" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
  
2. Change directory into the project folder
3. Create virtual environment<br>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>py -m venv venv
venv/Scripts/activate
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="py -m venv venv
venv/Scripts/activate" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>

  <p dir="auto">To get started, simply run the <code>main.py</code> file. The app will launch and display the starting screen:</p>
  
## GUI layout
<br>
<img width="414" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/ff6734e9-fac6-481d-8995-ac7e9f4a3866">
  <br>
  <br>
An simple interface allows the user to select the image to edit from the device and then applying the watermark in form of text and/or logo.<br><br>

<img width="414" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/ef6c28f3-05ce-4481-9ba5-b8e2cf0ecede">


## Add Text 
<img width="228" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/cb7732ce-cdde-4136-886d-4e1d41b18188">

<br>
<br>
The user can custom the watermark to add in the image.

## Add Image 
<img width="197" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/10e769f6-a171-4153-b56f-e2843b8fcd2e"><br>

If the user prefers also can add another logo or image to the original, choosing the size and transparency of the same.

## Save Image
<img width="414" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/857e5f9a-9012-4980-9bd7-7ec24b0936ee">
<br>
<br>
If each previous step is completed succesfully, the button will show a "✓". Then when pressing the button "Save", the new image will downloaded in the user device with the watermark added.

## Result
<img width="481" alt="image" src="https://github.com/tarintrader/Watermarking-App/assets/142015759/6f4f98d7-2582-4fbd-85f4-3f7aaaa683de">
<br>

## Dependencies

The Watermarking App uses the following libraries:
- Tkinter
- Pillow
- datetime
