# Expert_System/inference_engine.py
from typing import Dict, List, Set


def forward_chain(facts: Dict[str, bool], rules: List[tuple]) -> Set[str]:
    derived = set()
    working_facts = {key for key, value in facts.items() if value}

    for condition, conclusion in rules:
        if condition in working_facts:
            derived.add(conclusion)

    return derived
