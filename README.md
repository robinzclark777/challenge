# CSV to HTML generator

Reads .csv files downloaded from a google sheet and generates HTML. The google sheet is  
manually created from a summary of the monthly content from a large membership forum.  
There is a sheet for each year. Each sheet contains the following columns:

- month
- foundation skill
- advanced skill
- equipment setup details
- mindfulness
- league play small
- league play large
- league play international
- fitness

The html page will have the following structure:

- year
  - month
    - each of the above listed columns

The foundation skill, advanced skill, mindfulness, league play small, league play large,  
league play international, and fitness element will contain a description and a link to  
the page for that skill.

The equipment setup details will contain an image showing the general orientation of the setup, i.e.,  
where are the tunnels, contact obstacles, weave poles, and how many jumps are needed.  
The images will be drawn exquisitely by me and I can't draw.

There will be no styling because I hate css.

Future enhancements:

- programmically scrape website instead of manually creating google sheets
  OR
- allow for manual update of google sheet and programmatically generate and deploy
- html to actual website
- deploy html to a new, streamlined website targetted for mobile users
- use AI to create and send email to members about the new monthly content
