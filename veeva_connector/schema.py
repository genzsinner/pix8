from enum import Enum
from pydantic import BaseModel, Field


class FileDestinationEnum(str, Enum):
    s3 = "s3"


class DocumentMetaDataInputSchema(BaseModel):
    update_existing_data: bool = False
    destination: FileDestinationEnum = Field(
        description="Choose the destination type for the document metadata"
    )
