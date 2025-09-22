import os
import tweepy
import requests
import json
import random
from datetime import datetime
import logging
import time
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class IntelligentTwitterBot:
    def __init__(self):
        # Twitter API credentials
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        api_key = os.getenv("NEWSAPI_KEY")
        
        # OpenAI API for content generation
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        
        self.setup_twitter_api()
        logging.info("🧠 Intelligent Twitter Bot initialized!")
    
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
    
      def search_trending_topics(self):
        """Fetch real news headlines, add mirch-masala, and humanoid opinions"""
        url = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=5&apiKey={api_key}"

        try:
            response = requests.get(url)
            data = response.json()
            if data.get("status") != "ok":
                logging.error(f"❌ NewsAPI error: {data}")
                return {"key_insights": [], "actionable_steps": [], "tools_mentioned": [], "stats": ""}

            headlines = [article["title"] for article in data.get("articles", []) if article.get("title")]
            if not headlines:
                logging.warning("⚠ No headlines found, using fallback.")
                return {"key_insights": [], "actionable_steps": [], "tools_mentioned": [], "stats": ""}

            def add_masala_and_opinion(headline):
                spices = ["🔥 Breaking!", "💥 Kya baat!", "😲 OMG!", "🌟 Masala Alert:"]
                opinions = [
                    "Honestly, this feels like a big game-changer! 🤔",
                    "Not gonna lie, that’s surprising even for me. 😮",
                    "Kinda expected, but still spicy! 🌶️",
                    "If this continues, things could get wild. 😏"
                ]
                return f"{random.choice(spices)} {headline}\n🤖 Opinion: {random.choice(opinions)}"

            spiced_headlines = [add_masala_and_opinion(h) for h in headlines]

            # Adapt to your bot's format
            return {
                "key_insights": spiced_headlines,
                "actionable_steps": ["Stay tuned for more spicy updates!"],
                "tools_mentioned": ["NewsAPI.org"],
                "stats": "Live headlines fetched just now."
            }

        except Exception as e:
            logging.error(f"💥 Error fetching news: {e}")
            return {"key_insights": [], "actionable_steps": [], "tools_mentioned": [], "stats": ""}

    
    def generate_intelligent_content(self, research_data, post_time):
        """Generate intelligent, valuable content based on research"""
        
        insights = research_data["key_insights"]
        steps = research_data["actionable_steps"]
        tools = research_data["tools_mentioned"]
        stats = research_data["stats"]
        
        # Different content styles based on time
        if post_time == "morning":
            templates = [
                f"🌅 MORNING INSIGHT:\n\n{random.choice(insights)}\n\nHere's how to implement it:\n\n{chr(10).join(random.sample(steps, 3))}\n\nTools that help: {', '.join(random.sample(tools, 2))}\n\n#ProductivityTips #MorningMotivation",
                
                f"Good morning! 📈\n\nI researched the top productivity methods. This one shocked me:\n\n{random.choice(insights)}\n\nStep-by-step implementation:\n{chr(10).join(steps[:4])}\n\nStart today! #Productivity #Success",
                
                f"RESEARCH REVEALS: {stats}\n\nHere's the exact method:\n\n{chr(10).join(steps[:3])}\n\nBest tools to use:\n• {tools[0]}\n• {tools[1] if len(tools) > 1 else 'Google Calendar'}\n\nTry it for 7 days and watch the results! #GrowthHacks",
            ]
        
        elif post_time == "evening":
            templates = [
                f"🌆 EVENING WISDOM:\n\nToday I discovered something powerful:\n\n{random.choice(insights)}\n\nImplementation guide:\n{chr(10).join(steps[:3])}\n\nWhat will you implement tomorrow? #EveningReflection #Growth",
                
                f"End your day with this game-changer:\n\n{stats}\n\nHow to apply it:\n\n{chr(10).join(random.sample(steps, 3))}\n\nRecommended tools: {', '.join(random.sample(tools, 2))}\n\n#WisdomWednesday #PersonalGrowth",
                
                f"BREAKTHROUGH DISCOVERY: 🔍\n\n{random.choice(insights)}\n\nExact action plan:\n{chr(10).join(steps[:4])}\n\nStart tomorrow morning! #Research #ActionPlan"
            ]
        
        else:  # Manual/other times
            templates = [
                f"🔥 VIRAL INSIGHT:\n\n{random.choice(insights)}\n\nStep-by-step guide:\n{chr(10).join(steps[:3])}\n\nTools mentioned: {', '.join(tools[:2])}\n\n{stats}\n\n#Viral #Tips #HowTo",
                
                f"I analyzed 100+ case studies. This pattern emerged:\n\n{random.choice(insights)}\n\nImplementation:\n{chr(10).join(steps[:4])}\n\nGame-changing tools: {', '.join(tools[:2])}\n\n#Research #Strategy"
            ]
        
        return random.choice(templates)
    
    def create_thread_content(self, research_data):
        """Create detailed thread content for complex topics"""
        insights = research_data["key_insights"]
        steps = research_data["actionable_steps"]
        tools = research_data["tools_mentioned"]
        stats = research_data["stats"]
        
        thread_starter = f"🧵 THREAD: How to actually {random.choice(['increase productivity by 300%', 'build multiple income streams', 'grow your personal brand'])}:\n\n(Based on analyzing 100+ successful case studies)\n\n1/7"
        
        # This would be expanded for full thread functionality
        return thread_starter
    
    def post_tweet(self, content):
        """Post tweet with error handling"""
        try:
            # Ensure content is within Twitter's character limit
            if len(content) > 280:
                content = content[:275] + "..."
                logging.warning("Content truncated to fit Twitter limit")
            
            response = self.client.create_tweet(text=content)
            tweet_id = response.data['id']
            logging.info(f"✅ Tweet posted successfully! ID: {tweet_id}")
            return tweet_id
        except Exception as e:
            logging.error(f"❌ Error posting tweet: {e}")
            return None
    
    def run_intelligent_posting(self):
        """Main function for intelligent content posting"""
        try:
            current_hour = datetime.now().hour
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            logging.info(f"🕐 Starting intelligent research at: {current_time}")
            
            # Determine post time
            if current_hour == 5 or current_hour == 23:  # 5 AM IST
                post_time = "morning"
            elif current_hour == 17 or current_hour == 11:  # 5 PM IST  
                post_time = "evening"
            else:
                post_time = "manual"
                logging.info(f"🧪 Manual test run at hour {current_hour}")
            
            # Research trending topics
            logging.info("🔍 Starting topic research...")
            research_data = self.search_trending_topics()
            
            # Generate intelligent content
            logging.info("🧠 Generating intelligent content...")
            tweet_content = self.generate_intelligent_content(research_data, post_time)
            
            logging.info(f"📝 Generated intelligent tweet:\n{tweet_content}")
            
            # Post tweet
            tweet_id = self.post_tweet(tweet_content)
            
            if tweet_id:
                logging.info(f"🎉 Intelligent {post_time} tweet posted successfully!")
                logging.info(f"🔗 Tweet URL: https://twitter.com/user/status/{tweet_id}")
            else:
                logging.error(f"❌ Failed to post {post_time} tweet")
                
        except Exception as e:
            logging.error(f"💥 Error in intelligent posting: {e}")

def main():
    """Main function"""
    try:
        logging.info("🤖 Starting Intelligent Twitter Bot...")
        bot = IntelligentTwitterBot()
        bot.run_intelligent_posting()
    except Exception as e:
        logging.error(f"💥 Fatal error: {e}")

if __name__ == "__main__":
    main()
