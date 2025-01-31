from datetime import datetime
import enum
from pydantic import EmailStr, FutureDatetime
from sqlalchemy import TEXT
from sqlmodel import AutoString, Field, SQLModel, DATE  # type: ignore


class UserStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    WAITING = "WAITING"


class UserRole(enum.Enum):
    USER = "USER"
    DOCTOR = "DOCTOR"
    ADMIN = "ADMIN"


class AppointmentStatus(enum.Enum):
    pending = "pending"  # some or all participants have not finaized their acceptance of the AP
    booked = "booked"
    cancelled = "cancelled"
    postponed = "postponed"
    fulfilled = "fulfilled"
    noshow = "no show"  # some or all participants have not/did appear for the AP, usually the patient
    arrived = "arrived"  # patient has arrived and is waiting to be seen
    checked_in = "checked-in"  # all pre-administrative work is complete and encounter is ready to begin
    waitlist = "waitlist"


class AppointmentType(enum.Enum):
    checkup = "checkup"
    emergency = "emergency"
    follow = "follow"
    routine = "routine"
    walk_in = "walk in"


class BookingChannel(enum.Enum):
    phone = "Phone"
    web = "Web"


class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    PREFER_NOT_TO_SAY = "PREFER NOT TO SAY"
    NON_BINARY = "NON-BINARY"


class Users(SQLModel, table=True):
    # # user_id will be generated by the db, not by our code. Hence why it is declared as optional.
    user_id: int | None = Field(default=None, primary_key=True)  # get from firebase
    user_role: UserRole  # get from firebase
    name: str
    gender: Gender
    # date_of_birth: NaiveDatetime = Field(sa_type=DATETIME)
    # # = Field(sa_type=DATE) test this
    email: EmailStr = Field(index=True, sa_type=AutoString)  # get from firebase
    # created_at_utc: PastDatetime = Field(sa_type=DATETIME)
    # updated_at_utc: NaiveDatetime = Field(sa_type=DATETIME)
    # last_login_time: NaiveDatetime = Field(sa_type=DATETIME)
    country: str
    status: UserStatus  # frontend
    email_verified: bool  # get from firebase
    is_pregnant: bool
    pregnancy_trimester: str | None
    # TODO write calc logic later and remove None possibility
    # pregnancy_duration: NaiveDatetime = Field(sa_type=DATETIME)


# pregnancy_due_date_utc: FutureDatetime = Field(
#     sa_type=DATE
# )  # infer from current pregnancy conception info


class Doctors(SQLModel, table=True):
    # user_id will be generated by the db, not by our code. Hence why it is declared as optional.

    active: bool
    district: str  # district in which Doctor is located
    doctor_id: int | None = Field(default=None, primary_key=True)
    specialty: str
    practicing_from: datetime = Field(sa_type=DATE)


class Appointment(SQLModel, table=True):
    # user_id will be generated by the db, not by our code. Hence why it is declared as optional.

    appointment_id: int | None = Field(default=None, primary_key=True)
    # user_id: int = Field(foreign_key=True)
    # doctor_id: int = Field(foreign_key=True)
    start_time: datetime = Field(sa_type=DATE)
    end_time: datetime = Field(sa_type=DATE)
    date_created: datetime = Field(sa_type=DATE)
    duration: int
    appointment_date: FutureDatetime = Field(sa_type=DATE)
    status: AppointmentStatus
    observation: str
    user_instructions: str
    description: datetime = Field(sa_type=TEXT)
    appointment_booking_channel: BookingChannel
    cancellation_reason: str

    # VARCHAR VS TEXT
    # DOES SQLLITE support varchar and boolean
