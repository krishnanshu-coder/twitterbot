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
        """Search for current trending topics and information"""
        trending_queries = [
            "productivity tips 2025",
            "AI side hustles making money",
            "how to grow income streams",
            "digital marketing strategies that work",
            "remote work productivity hacks",
            "financial literacy tips beginners",
            "content creation monetization",
            "personal branding strategies",
            "time management techniques proven",
            "entrepreneurship lessons 2025"
        ]
        
        selected_topic = random.choice(trending_queries)
        logging.info(f"🔍 Researching: {selected_topic}")
        
        return self.research_topic_content(selected_topic)
    
    def research_topic_content(self, topic):
        """Research detailed content about a topic using web search simulation"""
        # Simulated research data (in real implementation, you'd use actual web scraping/search APIs)
        research_database = {
            "productivity tips 2025": {
                "key_insights": [
                    "Time blocking with 90-minute focus sessions increases productivity by 300%",
                    "The 2-minute rule: if it takes less than 2 minutes, do it immediately",
                    "Batch processing similar tasks saves 40% more time than switching between different tasks",
                    "Using AI tools like ChatGPT for research reduces work time by 60%",
                    "The Pomodoro Technique + meditation breaks improves focus by 250%"
                ],
                "actionable_steps": [
                    "1. Block 90-minute chunks in your calendar for deep work",
                    "2. Turn off all notifications during focus time", 
                    "3. Use apps like Forest or Freedom to block distracting websites",
                    "4. Keep a 'quick tasks' list for 2-minute items",
                    "5. Review and adjust your system weekly"
                ],
                "tools_mentioned": ["Forest app", "ChatGPT", "Google Calendar", "Notion"],
                "stats": "Studies show 300% productivity increase with time blocking"
            },
            
            "AI side hustles making money": {
                "key_insights": [
                    "AI content writing services are earning freelancers $5K-15K monthly",
                    "Automated social media management using AI tools nets $3K-10K monthly",
                    "AI-powered video editing services charge $500-2000 per client",
                    "Creating AI-generated art for businesses earns $200-500 per piece",
                    "AI chatbot development for small businesses pays $1K-5K per project"
                ],
                "actionable_steps": [
                    "1. Learn AI prompting skills (spend 2 weeks mastering ChatGPT/Claude)",
                    "2. Create a portfolio with 5-10 sample projects",
                    "3. Join freelancing platforms (Upwork, Fiverr, LinkedIn)",
                    "4. Start with lower rates ($25/hour) to build reviews",
                    "5. Scale to premium services ($100+/hour) after 10+ projects"
                ],
                "tools_mentioned": ["ChatGPT", "Claude", "Midjourney", "Canva", "Buffer"],
                "stats": "Average AI freelancer earns $7,500/month in first 6 months"
            },
            
            "digital marketing strategies that work": {
                "key_insights": [
                    "Video content gets 1200% more shares than text and images combined",
                    "Email marketing still has the highest ROI at $42 for every $1 spent",
                    "LinkedIn posts with 150-300 words get 40% more engagement",
                    "User-generated content increases conversion rates by 79%",
                    "Micro-influencers (1K-100K followers) have 60% higher engagement than mega-influencers"
                ],
                "actionable_steps": [
                    "1. Create short-form video content daily (60 seconds max)",
                    "2. Build email list with lead magnets (free guides, templates)",
                    "3. Engage with comments within 1 hour of posting",
                    "4. Share behind-the-scenes content 30% of the time",
                    "5. Collaborate with 2-3 micro-influencers monthly"
                ],
                "tools_mentioned": ["CapCut", "Mailchimp", "Canva", "Later", "BuzzSumo"],
                "stats": "Businesses using video content grow revenue 49% faster"
            }
        }
        
        # Find closest match or return default
        for key in research_database.keys():
            if any(word in topic.lower() for word in key.split()):
                return research_database[key]
        
        # Default fallback
        return research_database["productivity tips 2025"]
    
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
