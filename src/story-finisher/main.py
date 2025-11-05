import os
import re
from dotenv import load_dotenv
from crew import StoryFinisherCrew

load_dotenv()
os.makedirs("output", exist_ok =True)

def run():
    story_line = "He kept his last voicemail saved for five years, but today he finally pressed delete..."
    story_crew = StoryFinisherCrew()

    output = story_crew.crew().kickoff(inputs={"story_line": story_line})

    title = re.search(r'Title:\s*(.+)', str(output)).group(1).strip()
    filename = title.replace(' ', '_').replace(':', '').replace('/', '')
    open(f"output/{filename}.txt", 'w').write(str(output))

    # print("The final Story is : \n", output)


if __name__ =='__main__':
    run()