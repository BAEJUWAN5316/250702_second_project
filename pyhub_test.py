import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from pyhub.llm import OpenAILLM, UpstageLLM
from pydantic import BaseModel
from django.conf import settings
from blog.models import Post

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    model="gpt-4o",
    system_prompt="""
        너는 멋쟁이 시인이야. 유저의 설문조사 답변을 보고 멋진 닉네임을 지어줘!
        영어로 공백을 포함한 1글자~15글자로 어울리게 만들어주면 돼.
    """,
    max_tokens=20
)

keyword = [
    "당당한",
    "비겁한"
]

reply = llm.ask("난 멋져, 쿨해, 행복해지고싶어")

print(reply)