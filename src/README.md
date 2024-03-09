[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 💎 **ETIMO DIAMONDS**

Diamonds is a programming challenge. Program a bot and compete to get the highest score. For more information:

- [Project Specification](https://docs.google.com/document/d/13cbmMVXviyu8eKQ6heqgDzt4JNNMeAZO/edit)
- [Get Started with Diamonds](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit)

## **DESKRIPSI TUGAS** 
Diamonds merupakan suatu programming challenge yang mempertandingkan bot yang anda buat dengan bot dari para pemain lainnya. Setiap pemain akan memiliki sebuah bot dimana tujuan dari bot ini adalah mengumpulkan diamond sebanyak-banyaknya. Cara mengumpulkan diamond tersebut tidak akan sesederhana itu, tentunya akan terdapat berbagai rintangan yang akan membuat permainan ini menjadi lebih seru dan kompleks. Untuk memenangkan pertandingan, setiap pemain harus mengimplementasikan strategi tertentu pada masing-masing botnya.

## **IMPLEMENTASI ALGORITMA GREEDY** 
Dalam implementasi algoritma greedy pada permainan Diamonds, pendekatan yang digunakan bertujuan untuk memaksimalkan poin yang dapat diperoleh oleh bot. Algoritma ini mendasarkan setiap keputusannya pada informasi yang tersedia pada saat itu juga. Dengan demikian, algoritma memilih langkah yang terbaik atau paling menguntungkan pada setiap gilirannya berdasarkan kondisi saat ini.

## **HOW TO RUN THIS PROGRAM** 
### **GAME ENGINE SETUP**
#### Install Requirements
- Node.js (https://nodejs.org/en) 
- Docker desktop (https://www.docker.com/products/docker-desktop/) 
- Yarn
   ```
   npm install --global yarn
   ```

#### Installation & Configurations
1. Download [source code (.zip)](https://drive.google.com/file/d/1Sjuwsmi0eJg50SJEDN6OpAmShufLLAT2/view?usp=drive_link)
2. Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal
3. Masuk ke root directory dari project
4. Install dependencies menggunakan Yarn
   ```
   yarn
   ```
5. Setup default environment variable dengan menjalankan script berikut
- Untuk Windows
   ```
   ./scripts/copy-env.bat
   ```
- Untuk Linux
   ```
   chmod +x ./scripts/copy-env.sh
   ./scripts/copy-env.sh

   ```
6. Setup local database (buka aplikasi docker desktop terlebih dahulu, lalu jalankan command berikut di terminal)
   ```
   docker compose up -d database

   ```
7. Lalu jalankan script berikut. 
- Untuk Windows
   ```
   ./scripts/setup-db-prisma.bat

   ```
- Untuk Linux / (possibly) macOS
   ```
   chmod +x ./scripts/setup-db-prisma.sh
   ./scripts/setup-db-prisma.sh

   ```
#### Build
   ```
   npm run build

   ```
#### Run
   ```
   npm run start

   ```
Kunjungi frontend melalui http://localhost:8082/.

### **BOT STARTER PACK SETUP**
#### Install Requirements
- Python (https://www.python.org/downloads/)

#### Installation & Configurations
1. Download [source code (.zip)](https://drive.google.com/file/d/18zonuTVDvMENPtazyM1D9acUVdLNU2nz/view?usp=sharing)
2. Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal
3. Masuk ke root directory dari project
4. Install dependencies menggunakan pip
   ```
   pip install -r requirements.txt
   ```
#### Run
1. To run one bot

   ```
   python main.py --logic Greedy --email=queen@email.com --name=queen --password=123456 --team etimo
   ```

2. To run multiple bots simultaneously

   For Windows

   ```
   ./run-bots.bat
   ```

   For Linux / (possibly) macOS

   ```
   ./run-bots.sh
   ```

   <b>Before executing the script, make sure to change the permission of the shell script to enable executing the script (for linux/macOS)</b>

   ```
   chmod +x run-bots.sh
   ```

#### Note:

- If you run multiple bots, make sure each emails and names are unique
- The email could be anything as long as it follows a correct email syntax
- The name, and password could be anything without any space

## **AUTHOR** 
- 13522131 | [Owen Tobias Sinurat](https://github.com/owenthe10x)
- 13522140 | [Yasmin Farisah Salma](https://github.com/caernations)
- 13522139 | [Attara Majesta Ayub](https://github.com/attaramajesta)

## Credits 🪙

This repository is adapted from https://github.com/Etimo/diamonds2

Some code in this repository is adjusted to fix some issues in the original repository and to adapt to the requirements of Algorithm Strategies course (IF2211), Informatics Undergraduate Program, ITB.

©️ All rights and credits reserved to [Etimo](https://github.com/Etimo)
