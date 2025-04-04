import requests
from datetime import datetime, timedelta

def is_new_job(creation_date: str) -> bool:
    creation_date = datetime.fromisoformat(creation_date)
    current_date = datetime.now(creation_date.tzinfo)

    time_difference = current_date - creation_date
        
    if time_difference < timedelta(days=2):
        return True
    else: 
        return False
    

url = "https://api.remotar.com.br/jobs?search=&tagId=17&categoryId=4,7,15,13,14"
response = requests.get(url)

data = response.json()
jobs_list = data.get("data", [])

for job in jobs_list:
    creation_date = job.get("createdAt")
        
    if is_new_job(creation_date):
        title = job.get("title")
        description = job.get("description")       
        link = job.get("externalLink")

        company = job.get("company")
        company_name = company.get("name")

        print(f"""
              A empresa {company_name} anunciou uma nova vaga para {title}! ✨✨

                    🧑‍🎓 Nível: Júnior
                    📍 Localidade: Remoto

                    Descrição da vaga:

                    {description}

                    
                    🌐 Link: {link}

                    Caso decida se inscrever, não esqueça de personalizar seu currículo! 😉

                    Que a sorte esteja sempre a seu favor! 🤗
              """)