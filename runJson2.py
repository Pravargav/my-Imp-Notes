from faker import Faker
import random

fake = Faker()

def generate_paragraph():
    words = [fake.word() for _ in range(100)]

    paragraph = ' '.join(words)
    
    return paragraph

paragraphs = [generate_paragraph() for _ in range(10)]

print(paragraphs)
