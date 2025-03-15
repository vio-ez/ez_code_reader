import os 
from openai import OpenAI

model_name = os.environ.get('MODEL_NAME', '') 
llm_key = os.environ.get('LLM_KEY', '') 
base_url = os.environ.get('BASE_URL', '') 

client = OpenAI(
  base_url=base_url,
  api_key=llm_key
)


def read_code(system_prompt, user_prompt): 
    if len(user_prompt) < 3:return ''  

    try: 
        completion = client.chat.completions.create(
            model=model_name, 
            messages=[
                {"role": "system", "content": system_prompt }, 
                {"role": "user", "content": user_prompt }  
            ] 
        )

        content = completion.choices[0].message.content 
        return content
    
    except Exception as err:
        print('xx ', err, '\nxx ',user_prompt )
        return '' 



