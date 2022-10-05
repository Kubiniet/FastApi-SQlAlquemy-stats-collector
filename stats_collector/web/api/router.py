from fastapi.routing import APIRouter

from stats_collector.web.api import stats

api_router = APIRouter()
api_router.include_router(stats.router, prefix="/stats", tags=["stats"])
