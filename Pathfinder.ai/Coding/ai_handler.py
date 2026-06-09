import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AIHandler:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if self.api_key:
            self.client = Groq(api_key=self.api_key)
        else:
            self.client = None

    def analyze_market(self, topic, lang):
        if not self.client:
            return {"error": "API Key tidak dijumpai."}
        
        # System prompt menetapkan personaliti AI sebagai Pakar Kerjaya & Akademik
        system_prompt = """
        Anda adalah pakar perunding kerjaya dan akademik pintar untuk 'HalaTuju Programme'. 
        Tugas anda adalah menganalisis minat, subjek kegemaran, atau cita-cita yang dimasukkan oleh pelajar.
        Berikan respons yang mengandungi cadangan kursus (utamakan UKM jika sesuai), trend industri, analisis SWOT pelajar, dan bidang alternatif.
        """

        # Prompt ini memaksa Groq memulangkan format JSON dengan kunci (keys) yang betul
        prompt = f"""
        Analisis mendalam hala tuju akademik dan kerjaya untuk input: '{topic}'.
        Sila berikan output dalam format JSON SAHAJA dengan struktur berikut:
        {{
            "skor_kesesuaian": "Skor 0-100 berdasarkan kesesuaian minat/cita-cita dengan bidang {lang}",
            "status_trend_kerjaya": "Sila nyatakan status trend pekerjaan bidang ini (cth: Sangat Diperlukan) dalam {lang} ",
            "cadangan_kursus_universiti": "Senaraikan dengan nombor, 5  jenis kursus dan nama singkatan universiti yang berkaitan di universiti (utamakan Universiti Kebangsaan Malaysia - UKM jika sesuai) Pastikan ada satu baris kosong (selang satu baris) antara setiap nama universiti dalam {lang}",
            "prospek_kerjaya": "Ulasan padat tentang peluang pekerjaan dan bidang tugas masa depan dalam {lang}",
            "swot_pelajar": {{
                "kekuatan": ["Kelebihan/kemahiran yang perlu ada 1", "Kelebihan/kemahiran yang perlu ada 2"],
                "kelemahan": ["Cabaran diri/kekangan yang perlu diatasi 1", "Cabaran diri/kekangan yang perlu diatasi 2"],
                "peluang": ["Peluang industri/biasiswa/perkembangan 1", "Peluang industri/biasiswa/perkembangan 2"],
                "ancaman": ["Ancaman lambakan graduan/automasasi AI/persaingan 1", "Ancaman lambakan graduan/automasasi AI/persaingan 2"]
            }},
            "bidang_sampingan_disyorkan": {{
                "nama_bidang": "Nama bidang alternatif/interdisiplinari yang sepadan dengan minat mereka (cth: Bioinformatik, Digital Marketing, dll)",
                "sebab_disyorkan": "Kenapa bidang ini bagus untuk masa depan mereka dalam {lang}",
                "contoh_kerjaya": ["Kerjaya Alternatif 1", "Kerjaya Alternatif 2"]
            }},
            "nasihat_akademik": "Ulasan, langkah persediaan awal, atau nasihat motivasi untuk pelajar dalam {lang}"
        }}
        PENTING: Jangan sertakan sebarang teks pengenalan atau penutup (seperti ```json ... ```). 
        Kembalikan rentetan (string) JSON yang sah SAHAJA. Semua teks ulasan mestilah dalam {lang}.
        """

        try:
            # FIX: Properly indented this entire block to sit inside the try block
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3, # Nilai rendah supaya AI patuh pada format JSON
                response_format={"type": "json_object"} # Memaksa output JSON dari Groq
            )
            
            # Tukar string jawapan kepada Python Dictionary
            result_json = json.loads(response.choices[0].message.content)
            return result_json

        except Exception as e:
            return {"error": f"Gagal menghubungi AI: {str(e)}"}