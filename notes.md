
# Notes

```python

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    messages: List["Message"] = Relationship(back_populates="author")
    name: str

class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()))
    messages: List["Message"] = Relationship(back_populates="session")
    
    channel_id: str
    is_dm: bool

    deleted: bool = Field(default=False)

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    text: str
    
    session_id: Optional[int] = Field(default=None, foreign_key="session.id")
    session: Optional[Session] = Relationship(back_populates="messages")

    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="messages")

```
