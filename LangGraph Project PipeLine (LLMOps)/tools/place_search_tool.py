import os
from utils.place_info_search import TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        # Only use Tavily search, remove Google Places dependency
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place using Tavily search"""
            try:
                result = self.tavily_search.tavily_search_attractions(place)
                return f"Following are the attractions of {place}: {result}"
            except Exception as e:
                return f"Error searching attractions: {str(e)}"

        @tool  
        def search_restaurants(place: str) -> str:
            """Search restaurants in a place using Tavily search"""
            try:
                result = self.tavily_search.tavily_search_restaurants(place)
                return f"Following are the restaurants of {place}: {result}"
            except Exception as e:
                return f"Error searching restaurants: {str(e)}"

        @tool
        def search_activities(place: str) -> str:
            """Search activities in a place using Tavily search"""
            try:
                result = self.tavily_search.tavily_search_activity(place)
                return f"Following are the activities in and around {place}: {result}"
            except Exception as e:
                return f"Error searching activities: {str(e)}"

        @tool
        def search_transportation(place: str) -> str:
            """Search transportation options in a place using Tavily search"""
            try:
                result = self.tavily_search.tavily_search_transportation(place)
                return f"Following are the modes of transportation available in {place}: {result}"
            except Exception as e:
                return f"Error searching transportation: {str(e)}"

        return [search_attractions, search_restaurants, search_activities, search_transportation]