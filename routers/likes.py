
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from utils.auth import get_current_user

from datetime import datetime


router = APIRouter(prefix="", tags=["likes"])

def _parse_dt(dt: Optional[str]) -> Optional[datetime]:
    # from/to가 들어오면 ISO8601(date-time)로 파싱.
    if not dt:
        return None
    try:
        return datetime.fromisoformat(dt)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid date-time format (ISO8601 required)")


def _post_in_range():
    pass

# 좋아요 등록
@router.post("/posts/{postId}/likes")
def like_post(post_id: int, user=Depends(get_current_user)):
    pass

# 좋아요 취소
@router.delete("/posts/{postId}/likes")
def unlike_post(post_id: int, user=Depends(get_current_user)):
    pass


