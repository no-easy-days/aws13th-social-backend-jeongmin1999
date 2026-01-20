# app/routers/comments.py
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.comment import CommentCreate, CommentOut
from utils.data import read_json, write_json, next_id
from utils.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["comments"])

# 댓글 목록 조회
@router.get("/{post_id}/comments")
def list_comments():
    pass

# 댓글 작성
@router.post("/{post_id}/comments")
def create_comment():
    pass
