

from supabase import create_client

from dotenv import load_dotenv
import os
from fastapi.encoders import jsonable_encoder
import dataService

class BuilderDef():    

    def getSupabaseClient():
        supabase = create_client(
                os.getenv("SUPABASE_BASE_URL"),
                os.getenv("SUPABASE_SERVICE_KEY")
            )
        return supabase

    async def create_challengeAll(challengeAll: dataService.ChallengeAll):
        try:

            print("create_challenge reached here")
            # Initialize Supabase client
            challenge = dataService.Challenge(
                sponsor_id=challengeAll.sponsor_id,
                status_id=challengeAll.status_id,
                title=challengeAll.title,
                overview=challengeAll.overview,
                problem_statement=challengeAll.problem_statement,
                start_date=challengeAll.start_date,
                close_date=challengeAll.close_date,
                scope_exclusions=challengeAll.scope_exclusions,
                guidlines=challengeAll.guidlines,
                uploads=challengeAll.uploads,
                rewards_id=1,
                appType_id=challengeAll.appType_id,
                win_declare_date=challengeAll.win_declare_date
            )

            rewards = dataService.Rewards(
                reward_type_id=challengeAll.reward_type_id, 
                sponsor_id=challengeAll.sponsor_id,
                description=challengeAll.description,
                value=challengeAll.value
            )
            
            supabase = BuilderDef.getSupabaseClient()
            # Convert the challenge data to JSON-serializable format
            data = jsonable_encoder(rewards)
            result = supabase.table("rewards").insert(data).execute()
            print("Rewards",result)
            print("rewards created!")
            challenge.rewards_id = result.data[0]['id']
        
            data = jsonable_encoder(challenge)
            result = supabase.table("challenge").insert(data).execute()
            print("Challenge created here")
            return {
                "status": "success",
                "message": "Challenge created successfully",
                "data": result.data
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
        
    async def create_reward(rewards: dataService.Rewards):
        try:
            supabase = BuilderDef.getSupabaseClient()
            data = jsonable_encoder(rewards)
            result = supabase.table("rewards").insert(data).execute()
            return {
                "status": "success",
                "message": "Challenge created successfully",
                "data": result.data
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
        
    async def get_challenges():
        try:          
            supabase = BuilderDef.getSupabaseClient()
            result = supabase.table("view_challenge").select("*").execute()            
            return {
                "status": "success",
                "message": "Challenges retrieved successfully",
                "data": result.data
            }            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }