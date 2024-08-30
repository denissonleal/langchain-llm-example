from dotenv import load_dotenv
import os

load_dotenv()
os.getenv('OPENIA_API_KEY')

config = {
    'app_env': os.getenv('APP_ENV', default='prod'),
    'llm_api_model': os.getenv('LLM_API_MODEL', default='gpt-3.5-turbo'),
    'llm_api_key': os.getenv('LLM_API_KEY'),
    'embeddings_model': os.getenv('EMBEDDINGS_MODEL', default='gpt-3.5-turbo'),
}

if __name__ == '__main__':
    print(config)
