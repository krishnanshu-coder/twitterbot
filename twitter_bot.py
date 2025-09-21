import os
import tweepy
import random
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SmartTwitterBot:
    def __init__(self):
        # Load Twitter API credentials
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        self.setup_twitter_api()
        logging.info("🔥 Smart Twitter Bot initialized!")
    
    def setup_twitter_api(self):
        """Setup Twitter API"""
        try:
            if not all([self.api_key, self.api_secret, self.access_token, 
                       self.access_token_secret, self.bearer_token]):
                raise ValueError("Missing Twitter API credentials")
            
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                wait_on_rate_limit=True
            )
            
            logging.info("✅ Twitter API connected")
            
        except Exception as e:
            logging.error(f"❌ Twitter API error: {e}")
            raise
    
    def get_dynamic_variables(self):
        """Variables to make tweets unique and fresh"""
        return {
            'years': ['2024', '2025', '2030'],
            'amounts': ['$10K', '$50K', '$100K', '$500K'],
            'timeframes': ['30 days', '6 months', '1 year', '2 years'],
            'industries': ['marketing', 'sales', 'design', 'content creation', 'consulting'],
            'skills': ['AI prompting', 'data analysis', 'content writing', 'social media', 'copywriting'],
            'tools': ['ChatGPT', 'Notion', 'Canva', 'LinkedIn', 'Twitter'],
            'books': ['Atomic Habits', 'Think and Grow Rich', 'The 7 Habits', 'Rich Dad Poor Dad'],
            'numbers': ['3', '5', '7', '10', '12'],
            'current_day': datetime.now().strftime('%A'),
            'current_month': datetime.now().strftime('%B'),
            'current_year': datetime.now().year
        }
    
    def generate_fresh_tweet(self, template_category, post_time):
        """Generate fresh, dynamic tweets using templates + variables"""
        variables = self.get_dynamic_variables()
        
        templates = {
            "morning": [
                f"Good morning! 🌅\n\nThe difference between people who make {random.choice(variables['amounts'])} vs {random.choice(variables['amounts'])} annually:\n\n• Lower: Work harder\n• Higher: Work smarter\n\nStop trading time for money. Start building systems.\n\n#MondayMotivation #Success",
                
                f"I wish someone told me this at 20:\n\nYour network determines your net worth, but your habits determine both.\n\n• Show up consistently\n• Add value first  \n• Follow up always\n\nRelationships compound like interest over {random.choice(variables['timeframes'])}.\n\n#LifeLessons #Success",
                
                f"{random.choice(variables['numbers'])} skills that will make you irreplaceable by {random.choice(variables['years'])}:\n\n1. {random.choice(variables['skills'])}\n2. Systems thinking\n3. Emotional intelligence\n4. Cross-cultural communication\n5. Problem solving\n\nStart building these TODAY.\n\n#FutureSkills #CareerGrowth",
                
                f"I studied 100+ successful people in {random.choice(variables['industries'])} and found these patterns:\n\n• They read daily\n• They wake up early\n• They exercise regularly\n• They invest in relationships\n• They never stop learning\n\nSuccess leaves clues. Follow them.\n\n#Success #Habits",
                
                f"The ${random.choice(['5', '10', '20'])} investment that changed my perspective:\n\n'{random.choice(variables['books'])}' audiobook\n\nBefore: Scattered, reactive, busy\nAfter: Focused, proactive, productive\n\nSmall investments, massive returns.\n\n#PersonalDevelopment #Books"
            ],
            
            "evening": [
                f"End your {variables['current_day']} with this realization:\n\nYour biggest competitor isn't someone else.\n\nIt's who you were yesterday.\n\nEvery day is a chance to level up {random.choice(['1%', '2%', '5%'])}.\n\n#Growth #Mindset #SelfImprovement",
                
                f"The psychology trick that makes people instantly like you:\n\nRemember their name + use it {random.choice(['3', '5'])} times in conversation.\n\n'Thanks, Sarah!' hits different than just 'Thanks!'\n\nPeople's favorite sound? Their own name.\n\n#Psychology #Networking #Communication",
                
                f"Nobody prepared me for how this hits different at {random.choice(['25', '30', '35'])}:\n\nRealizing 'busy' and 'productive' are opposite things.\n\nBusy = Motion without progress\nProductive = Progress with purpose\n\nChoose wisely tomorrow.\n\n#Productivity #LifeLessons",
                
                f"I tried this productivity method for {random.choice(variables['timeframes'])}. Results:\n\n• {random.choice(['2x', '3x', '5x'])} more focused work\n• {random.choice(['40%', '50%', '60%'])} less stress\n• Way better results\n\nThe method: Time blocking + deep work\n\nSmall changes, massive impact.\n\n#Productivity #Focus",
                
                f"The book that changed my entire mindset in 24 hours:\n\n'{random.choice(variables['books'])}'\n\nKey insight: You don't rise to your goals, you fall to your systems.\n\nStop setting goals. Start building systems.\n\n#BookRecommendation #SystemsThinking"
            ],
            
            "ai_tech": [
                f"Nobody talks about this, but AI just changed everything in {random.choice(variables['industries'])}...\n\nWhat used to take {random.choice(['10 hours', '5 hours', '8 hours'])} now takes {random.choice(['10 minutes', '30 minutes', '1 hour'])}.\n\nThe question: 'Will someone using AI replace me?'\n\n#AI #Future #Technology",
                
                f"{random.choice(variables['numbers'])} AI side hustles making people {random.choice(variables['amounts'])}+/month:\n\n1. AI-powered {random.choice(['content writing', 'social media'])}\n2. Automated {random.choice(['email marketing', 'customer service'])}\n3. AI chatbot development\n4. Voice-over generation\n5. Image creation services\n\nThe opportunity is NOW.\n\n#AI #SideHustle #Entrepreneurship",
                
                f"I asked {random.choice(variables['tools'])} to analyze my business plan. Results:\n\n✅ Found {random.choice(['5', '7', '10'])} flaws I missed\n✅ Suggested {random.choice(['8', '12', '15'])} improvements  \n✅ Predicted {random.choice(['3', '5', '7'])} risks\n\nAI isn't just a tool. It's a business partner.\n\n#AI #Business #ChatGPT",
                
                f"This AI trend will make {random.choice(['80%', '90%'])} of current jobs obsolete by {random.choice(variables['years'])}.\n\nBut here's the twist: It creates entirely new categories we can't imagine.\n\nAdapt or get left behind.\n\n#FutureOfWork #AI #Adaptation",
                
                f"The AI tool replacing entire {random.choice(['marketing', 'design', 'writing'])} teams:\n\n• Creates content in seconds\n• Designs visuals instantly\n• Analyzes data automatically\n• Optimizes performance real-time\n\nWe're changing the game completely.\n\n#AIRevolution #Marketing"
            ],
            
            "money_success": [
                f"I made {random.choice(variables['amounts'])} in {random.choice(variables['timeframes'])} selling this:\n\nDigital {random.choice(['templates', 'courses', 'coaching'])}.\n\n• Created once\n• Sold infinitely  \n• Zero inventory\n• Global reach\n\nThe internet rewards creators.\n\n#DigitalProducts #Entrepreneurship",
                
                f"The side hustle nobody talks about paying ${random.choice(['300', '500', '800'])}/day:\n\n{random.choice(['Content repurposing', 'Social media management', 'Email marketing'])}.\n\nEveryone needs it. Few have time for it.\n\nBe the solution.\n\n#SideHustle #FreelanceBusiness",
                
                f"Why everyone's quitting 9-5 for this in {variables['current_year']}:\n\nDigital products + Personal brand\n\n= Location freedom\n= Time freedom  \n= Financial freedom\n\nNew economy rewards value creators, not time traders.\n\n#DigitalNomad #Entrepreneurship",
                
                f"I analyzed {random.choice(['500', '1000'])} millionaires. What they ALL do:\n\n• Invest in assets, not liabilities\n• Build {random.choice(['3-5', '5-7'])} income streams\n• Prioritize learning over earning\n• Network intentionally\n• Start before feeling ready\n\n#WealthMindset #Success",
                
                f"Rich vs Wealthy people in {variables['current_year']}:\n\nRich: High income, high expenses\nWealthy: Multiple income streams, low expenses\n\nRich work for money.\nWealthy make money work for them.\n\n#FinancialLiteracy #WealthBuilding"
            ]
        }
        
        # Select appropriate template based on time
        if post_time == "morning":
            return random.choice(templates["morning"])
        elif post_time == "evening":
            return random.choice(templates["evening"])
        else:
            # Random selection from all categories
            all_tweets = []
            for category in templates.values():
                all_tweets.extend(category)
            return random.choice(all_tweets)
    
    def post_tweet(self, content):
        """Post tweet with error handling"""
        try:
            response = self.client.create_tweet(text=content)
            tweet_id = response.data['id']
            logging.info(f"✅ Tweet posted successfully! ID: {tweet_id}")
            return tweet_id
        except Exception as e:
            logging.error(f"❌ Error posting tweet: {e}")
            return None
    
    def run_scheduled_post(self):
        """Main function for scheduled posting"""
        try:
            current_hour = datetime.now().hour
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            logging.info(f"🕐 Current time: {current_time} (Hour: {current_hour})")
            
            # Determine post time
            if current_hour == 5 or current_hour == 23:  # 5 AM IST
                post_time = "morning"
            elif current_hour == 17 or current_hour == 11:  # 5 PM IST  
                post_time = "evening"
            else:
                post_time = "manual"
                logging.info(f"🧪 Manual test run at hour {current_hour}")
            
            logging.info(f"🎯 Generating {post_time} tweet...")
            
            # Generate fresh content
            tweet_content = self.generate_fresh_tweet("dynamic", post_time)
            
            logging.info(f"📝 Generated tweet:\n{tweet_content}")
            
            # Post tweet
            tweet_id = self.post_tweet(tweet_content)
            
            if tweet_id:
                logging.info(f"🎉 {post_time.title()} tweet posted successfully!")
                logging.info(f"🔗 Tweet URL: https://twitter.com/user/status/{tweet_id}")
            else:
                logging.error(f"❌ Failed to post {post_time} tweet")
                
        except Exception as e:
            logging.error(f"💥 Error in run_scheduled_post: {e}")

def main():
    """Main function"""
    try:
        logging.info("🤖 Starting Smart Twitter Bot...")
        bot = SmartTwitterBot()
        bot.run_scheduled_post()
    except Exception as e:
        logging.error(f"💥 Fatal error: {e}")

if __name__ == "__main__":
    main()
