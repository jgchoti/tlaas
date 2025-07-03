from fastapi import APIRouter, HTTPException, Query
from typing import List
import random
from model.excuse_models import ExcuseResponse, CustomExcuseRequest, CustomExcuseResponse
from data.excuses import excuses
from utils.refuse import api_refuse

router = APIRouter(prefix="/excuse", tags=["Excuses"])

@router.get("/", response_model=ExcuseResponse)
async def get_excuse():
    refusal = api_refuse()
    if refusal:
        return ExcuseResponse(
            excuse=refusal["excuse"],
            category="Who Care?",
            api_status=refusal.get("status")
        )
    excuse = random.choice(excuses)
    category = excuse["tags"][0] if excuse.get("tags") else "general"
    return ExcuseResponse(excuse=excuse["excuse"], category=category)
  

@router.get("/categories")
async def get_categories():
    refusal = api_refuse()
    if refusal:
        return refusal
    categories_set = set()
    for e in excuses:
        categories_set.update(e.get("tags", []))
    return {
        "categories": list(categories_set),
        "total_excuses": (len(categories_set))
    }

@router.get("/{category}", response_model=ExcuseResponse)
async def get_excuse_by_category(category: str,  tag: str = Query("general", description="Filter excuses by tag")):
    refusal = api_refuse()
    if refusal:
        return refusal
    categories_set = set(t for e in excuses for t in e.get("tags", []))
    filtered = [
        e for e in excuses 
        if category.lower() in (t for t in e.get("tags", []))
        and tag.lower() in (t for t in e.get("tags", []))
    ]
    if not filtered:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Ugh, no excuses found for category '{category}' with tag '{tag}'. "
                f"Maybe try one of these categories or tags instead: {sorted(categories_set)}? "
                "Or just skip it, I’m way too lazy to care."
            )
        )
    chosen = random.choice(filtered)
    return ExcuseResponse(excuse=chosen["excuse"], category=category)

@router.post("/custom", response_model=CustomExcuseResponse)
async def get_custom_excuse(payload: CustomExcuseRequest):
    refusal = api_refuse()
    if refusal:
        return refusal
    task = payload.task
    templates = [
        f"I was too busy researching about {task}.",
        f"I got distracted by the documentary about {task}.",
        f"I started doing {task} but fell asleep thinking about it.",
        f"The AI assistant told me to avoid {task} for mental health.",
        f"{task} sounded like a lot, so I didn’t.",
        f"I was waiting for the perfect moment to start {task}.",
        f"I was googling how to do {task} and got lost in cat videos.",
        f"The weather wasn't right for {task}.",
        f"I was building up mental energy for {task}.",
        f"My horoscope said to avoid {task} today.",
        f"I was procrastinating on {task} so efficiently that I forgot to do it.",
        f"The {task} tutorial was 47 minutes long, ain't nobody got time for that.",
        f"I was stress-eating about having to do {task}.",
        f"My lucky '{task}' socks were in the wash."
    ]
   
    excuse = random.choice(templates)
    return CustomExcuseResponse(
        excuses=excuse,
        topic=task,
        believability="Varies by audience"
    )
