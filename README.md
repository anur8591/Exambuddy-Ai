# 📚 ExamBuddy.AI

**AI-powered Vernacular Study Copilot** – Turn your syllabus into a personalized day-by-day exam plan with auto-generated quizzes in English/Hindi.  
Built for Indian students to revise smarter, faster, and with less stress — all via a simple web app (and soon WhatsApp).

---

## 📖 Overview

ExamBuddy.AI helps students **plan and revise their syllabus** in the most efficient way possible.  
You just upload your syllabus or notes (PDF/text), and ExamBuddy:
1. **Generates a personalized date-wise revision plan**.
2. **Creates topic-wise quizzes** for active recall learning.
3. **Supports multiple languages** (starting with English & Hindi).
4. (Coming soon) Works directly from WhatsApp for maximum accessibility.

This project is built for **Hack Node India 2025** (Track: *EdTech & Learning*),  
but it’s something I personally needed for my own exams.

---

## ✨ Features

- 📄 **PDF/Text Upload** – Import syllabus or notes easily.
- 🗓 **Smart Study Planner** – AI creates a day-by-day revision roadmap.
- 📝 **Auto Quiz Generator** – 5 MCQs per topic with explanations.
- 🌐 **Vernacular Support** – English & Hindi (more languages planned).
- 📱 **Mobile-First UI** – Simple and responsive design.
- 💾 **Decentralized Progress Tracking (Stretch)** – Store completion records on IPFS for verifiable credentials.

---

## 🛠 Tech Stack

**Backend**  
- Python 3.10+  
- FastAPI – API development  
- FAISS – Semantic search for syllabus chunks  
- PyMuPDF – PDF parsing  
- Local/Hosted LLM – Quiz & plan generation  

**Frontend**  
- Next.js – Web app  
- Tailwind CSS – Styling  
- React Hooks – State management  

**Optional Integrations**  
- Twilio / Meta WhatsApp API – WhatsApp chatbot  
- IPFS (Pinata/Web3.Storage) – Decentralized storage  

---

## 📦 Project Structure

