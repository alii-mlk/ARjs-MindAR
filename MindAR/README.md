# MindAR Frontend – Plant Health Recognition Project

## Description
This folder contains the MindAR-based frontend developed for our AFC course project.

The frontend is responsible for:
- Opening the camera
- Detecting the image target using MindAR
- Capturing the leaf region of interest (ROI)
- Sending the captured image to the backend server
- Displaying the returned prediction result

The main frontend file is `main.html`, and the image target data is stored in `targets.mind`.

---

## Important Note About Camera Permission
To use the camera in the browser, the project must be opened in a secure context.

That means:
- `localhost` works on the same computer
- `https://` is required when opening the project from another device such as a phone

Because of this, we must create a local HTTPS server.

---

## Creating HTTPS Certificates (mkcert)

To allow camera access from other devices (like a smartphone), we create local HTTPS certificates using **mkcert**.

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

This will generate certificate files like:
```
[your_ip]+1.pem
[your_ip]+1-key.pem
```

---

### Windows
Install **mkcert** and **Node.js** first, then run:
```
mkcert -install
mkcert [your_ip] localhost
```

Then start HTTPS server:
```
npx http-server . -p 9000 -S ^
 -C [your_ip]+1.pem ^
 -K [your_ip]+1-key.pem
```

---

## Running the MindAR Frontend (HTTPS Server)

After generating the certificates, run the HTTPS server using:

```
npx http-server . -p 9000 -S   -C [your_ip]+1.pem   -K [your_ip]+1-key.pem
```

Then open on your smartphone or another device:
```
https://[your_ip]:9000/main.html
```

Make sure:
- Phone and laptop are on the same WiFi network
- Allow camera permission in the browser
- Accept the certificate warning the first time

---

## Backend Connection
The frontend sends the captured ROI image to the backend API.

Inside `main.html`, this line defines the backend endpoint:
```
const API_URL = "http://localhost:8000/predict";
```

If using another device, replace `localhost` with your computer IP:
```
const API_URL = "http://[your_ip]:8000/predict";
```

---

## Workflow
1. Start the backend server.
2. Start the HTTPS server for the MindAR folder.
3. Open `main.html` through HTTPS.
4. Allow camera permission.
5. Show the target image to the camera.
6. Capture leaf ROI.
7. Send image to backend.
8. Display prediction result.

---

## Notes
- Camera access will not work over plain HTTP on mobile devices.
- Always use HTTPS when testing on smartphones.
- The laptop and phone must be connected to the same network.
