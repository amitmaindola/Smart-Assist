from question_answer.pipelines import pipeline1
nlp = pipeline1("question-generation")
# text = "People celebrate Holi with utmost fervour and enthusiasm, especially in North India. One day before Holi, people conduct a ritual called Holika Dahan. In this ritual, people pile heaps of wood in public areas to burn. It symbolizes the burning of evil powers revising the story of Holika and King Hiranyakashyap. Furthermore, they gather around the Holika to seek blessings and offer their devotion to God."

def generate_questions(text):
    return nlp(text)