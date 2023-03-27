def forward_chaining(knowledge_base, rules):
    inferred_facts = set()
    agenda = []

    # Add all known facts to the agenda
    for fact in knowledge_base:
        agenda.append(fact)

    # Loop until agenda is empty
    while agenda:
        # Get the next fact to process
        fact = agenda.pop(0)

        # Apply all rules that can be triggered by the fact
        for rule in rules:
            if all(condition in inferred_facts for condition in rule['conditions']):
                # All conditions are met, so infer the new fact
                new_fact = rule['conclusion']
                inferred_facts.add(new_fact)

                # Add new fact to agenda
                agenda.append(new_fact)

    # Return all inferred facts
    return inferred_facts
