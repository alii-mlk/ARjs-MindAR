# AR.js Frontend – Plant Health Recognition Project

## Description
This folder contains the AR.js-based frontend developed for the AFC project.

This version of the frontend uses **AR.js** for image tracking and augmented reality visualization in the browser.

The AR.js frontend is responsible for:
- Opening the camera
- Detecting the AR marker / image target
- Displaying AR content
- Capturing the leaf region of interest (ROI)
- Sending the captured image to the backend server
- Displaying the prediction result returned from the backend

---

## Important Note About Camera Permission
To access the camera in the browser, the application must run in a **secure context**.

This means:
- It works on `localhost`
- It works on `https://`
- It does NOT work on plain `http://` when opened from a phone

Therefore, when testing on a smartphone, we must run the project using an **HTTPS server**.

---

## Creating HTTPS Certificates (mkcert)

To run the AR.js project over HTTPS, we use **mkcert** to generate local SSL certificates.

### macOS
Install mkcert:
```
brew install mkcert
brew install nss   # only if you also use Firefox
```

Then install certificates and generate them:
```
mkcert -install
mkcert [your_ip] localhost
```

This will generate files like:
```
[your_ip]+1.pem
[your_ip]+1-key.pem
```

---

### Windows
Install **mkcert** and **Node.js**, then run:
```
mkcert -install
mkcert [your_ip] localhost
```

Start HTTPS server:
```
npx http-server . -p 9000 -S ^
 -C [your_ip]+1.pem ^
 -K [your_ip]+1-key.pem
```

---

## Running the AR.js Frontend (HTTPS Server)

After generating the certificates, start the HTTPS server:

```
npx http-server . -p 9000 -S   -C [your_ip]+1.pem   -K [your_ip]+1-key.pem
```

Then open in your phone browser:
```
https://[your_ip]:9000/index.html
```

Make sure:
- Phone and computer are connected to the same WiFi
- Allow camera permission
- Accept the certificate warning the first time

---

## Backend Connection
The AR.js frontend sends the captured ROI image to the backend API.

Inside the JavaScript file, the backend endpoint is defined like this:
```
const API_URL = "http://localhost:8000/predict";
```

If using a phone, replace `localhost` with your computer IP:
```
const API_URL = "http://[your_ip]:8000/predict";
```

---

## Workflow
1. Start the backend server.
2. Start the HTTPS server for the AR.js folder.
3. Open the AR page through HTTPS.
4. Allow camera permission.
5. Show the AR marker / image target.
6. Capture the leaf ROI.
7. Send image to backend.
8. Display prediction result.

---

## Notes
- Camera access will not work over HTTP on smartphones.
- Always use HTTPS for AR.js when testing on mobile devices.
- Make sure backend server is running before using the AR frontend.
