import pandas as pd
import random
import streamlit as st

# Function to create icebreakers
def generate_icebreaker(row, name_col, title_col, company_col=None):
    name = row[name_col]
    title = row[title_col]
    company = row[company_col] if company_col else ""
    
    icebreakers = [
        f"{name}, your impressive track record as {title} at {company} showcases your exceptional leadership in the industry. It's inspiring to see how your expertise is pushing boundaries and shaping the future.",
        f"As a {title} at {company}, {name}, you've demonstrated unmatched dedication and skill, creating real impact within your organization. Your journey is a testament to what great leadership can accomplish.",
        f"With your extensive experience as {title} at {company}, {name}, it's clear you are a catalyst for innovation. Your efforts are not only shaping the present but also defining the future of your industry.",
        f"Your role as {title} at {company}, {name}, shows your ability to consistently deliver excellence. It’s exciting to see how your leadership is steering your team toward success in a rapidly evolving market.",
        f"{name}, leading as {title} at {company}, you have clearly established yourself as a key driver of change in your industry. Your influence and strategic vision are making a powerful impact.",
        f"{name}, your expertise as {title} at {company} has proven to be a game-changer in your field. It's rare to find someone with such a profound understanding of the industry and the ability to turn that knowledge into action.",
        f"Your role as {title} at {company}, {name}, reflects your commitment to excellence and innovation. You are truly shaping the industry and inspiring others with your leadership and expertise.",
        f"As {title} at {company}, {name}, you've consistently demonstrated an ability to lead with vision and integrity. Your work is setting new standards and creating opportunities for others to follow.",
        f"Your leadership as {title} at {company}, {name}, speaks volumes about your ability to navigate challenges and deliver impactful results. You are truly an industry leader, creating meaningful change.",
        f"{name}, as {title} at {company}, you're redefining what it means to lead in your field. Your ability to foster growth and innovation is a true testament to your expertise and dedication.",
        f"{name}, your experience as {title} at {company} is truly commendable. It’s clear that you are not just managing but actively driving forward-thinking initiatives that make a real difference in your industry.",
        f"As {title} at {company}, {name}, your ability to manage and inspire your team is remarkable. It's clear you're a visionary, and your leadership is shaping the industry in profound ways.",
        f"With your role as {title} at {company}, {name}, you've proven time and time again that you're not just part of the industry but leading it forward. Your contributions are invaluable to your organization's success.",
        f"{name}, your leadership as {title} at {company} has been transformative, and it's exciting to see the direction you're heading. Your innovative approach is making waves and setting a new standard.",
        f"As {title} at {company}, {name}, you've established yourself as a pillar of innovation and success. Your work is a great example of how leadership and vision can truly elevate an entire industry.",
        f"{name}, your expertise as {title} at {company} is both rare and valuable. It's no wonder you're a respected figure in your field, pushing the boundaries of what's possible with your forward-thinking strategies.",
        f"{name}, leading as {title} at {company}, you're not only achieving success but also creating lasting impact. Your contributions to the industry are both innovative and deeply valuable.",
        f"Your experience as {title} at {company}, {name}, is a perfect blend of practical leadership and visionary thinking. You’re a true leader in every sense, with a remarkable ability to steer teams toward success.",
        f"{name}, your role as {title} at {company} is a true reflection of your ability to inspire and lead with purpose. It's evident that you are making an indelible mark on your field with your thoughtful approach.",
        f"{name}, your work as {title} at {company} continues to be a source of inspiration to many. Your leadership is not only about strategy but also about fostering an environment where teams thrive and succeed.",
        f"{name}, your experience as {title} at {company} is a testament to your dedication to the craft. You’ve demonstrated a remarkable ability to lead your team toward significant achievements and industry-leading results.",
        f"As {title} at {company}, {name}, your leadership and expertise are transforming the industry. You have a unique ability to drive results while keeping the bigger picture in mind—it's truly inspiring.",
        f"{name}, with your experience as {title} at {company}, you’ve truly mastered the art of leadership and innovation. Your work is shaping the way forward and paving the way for future success in your industry.",
        f"With your extensive background as {title} at {company}, {name}, it's evident that you're not just part of the industry—you’re an integral force driving change. Your leadership continues to make a significant impact.",
        f"{name}, your leadership as {title} at {company} demonstrates your ability to drive both innovation and success. You're not just leading the charge; you're setting a standard for others to follow.",
        f"Your expertise as {title} at {company}, {name}, is exactly what the industry needs right now. Your thoughtful approach and innovative solutions are positioning you as a true leader in your field.",
        f"{name}, as {title} at {company}, you’ve shown incredible resilience and vision. Your leadership is helping to create lasting change and is setting a new benchmark for success.",
        f"{name}, your experience as {title} at {company} speaks volumes about your ability to turn challenges into opportunities. It’s no wonder your leadership is admired across the industry.",
        f"{name}, leading as {title} at {company}, you continue to inspire others through your exceptional vision and dedication. Your leadership is not just about achieving results—it's about shaping the future of your industry.",
        f"As {title} at {company}, {name}, you’re clearly a driving force within your industry. Your innovative thinking and strategic leadership are paving the way for the next generation of success.",
        f"{name}, as {title} at {company}, you bring an incredible depth of experience and vision to your role. It's clear that your contributions are not just valuable—they're shaping the future of your field.",
        f"{name}, your work as {title} at {company} has undoubtedly had a lasting impact. It’s inspiring to see someone with such a deep understanding of the industry lead with both expertise and empathy.",
        f"As {title} at {company}, {name}, you bring a unique blend of insight and leadership to your role. It's no surprise that you're a key figure in shaping the future of your industry."
    ]
    
    return random.choice(icebreakers)

# Streamlit App
def main():
    st.title("Complimentary Icebreaker Generator")
    st.write("Upload your CSV file with names, job titles, and companies to generate personalized icebreakers.")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Ask user for column names for name, title, and company
        name_col = st.selectbox("Select the column for Name", df.columns)
        title_col = st.selectbox("Select the column for Job Title", df.columns)
        company_col = st.selectbox("Select the column for Company Name", df.columns)
        
        # Generate icebreakers for each row in the CSV file
        df['Icebreaker'] = df.apply(generate_icebreaker, axis=1, name_col=name_col, title_col=title_col, company_col=company_col)
        
        # Display results
        st.write(df[['Icebreaker']])
        
        # Download the updated CSV with icebreakers
        output_file = "icebreakers_output.csv"
        df.to_csv(output_file, index=False)
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download Icebreakers",
                data=file,
                file_name=output_file,
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
