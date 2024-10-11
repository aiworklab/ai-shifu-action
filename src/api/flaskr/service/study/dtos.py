# Description: This file contains the Data Transfer Objects (DTOs) for the study service.
# DTOs are used to transfer data between the service and the controller.
# @author geyunfei@gmail.com

from typing import List
from flaskr.common.swagger import register_schema_to_swagger
from flaskr.service.order.funs import AICourseLessonAttendDTO


@register_schema_to_swagger
class ScriptDTO:
    script_type: str  # "'text' 'input' 'buttons' 'text_end'"
    script_content: str
    script_id: str

    def __init__(self, script_type, script_content, script_id=None):
        self.script_type = script_type
        self.script_content = script_content
        self.script_id = script_id

    def __json__(self):
        return {
            "type": self.script_type,
            "content": self.script_content,
            "script_id": self.script_id,
        }


@register_schema_to_swagger
class AICourseLessonAttendScriptDTO:
    attend_id: str
    script_id: str
    lesson_id: str
    course_id: str
    user_id: str
    script_index: int
    script_role: str
    script_content: str
    status: str

    def __init__(
        self,
        attend_id,
        script_id,
        lesson_id,
        course_id,
        user_id,
        script_index,
        script_role,
        script_content,
        status,
    ):
        self.attend_id = attend_id
        self.script_id = script_id
        self.lesson_id = lesson_id
        self.course_id = course_id
        self.user_id = user_id
        self.script_index = script_index
        self.script_role = script_role
        self.script_content = script_content
        self.status = status

    def __json__(self):
        return {
            "attend_id": self.attend_id,
            "script_id": self.script_id,
            "lesson_id": self.lesson_id,
            "course_id": self.course_id,
            "user_id": self.user_id,
            "script_index": self.script_index,
            "script_role": self.script_role,
            "script_content": self.script_content,
            "status": self.status,
        }


@register_schema_to_swagger
class AILessonAttendDTO:
    lesson_no: str
    lesson_name: str
    lesson_id: str
    status: str
    children: List[AICourseLessonAttendDTO]
    status: str

    def __init__(
        self, lesson_no: str, lesson_name: str, lesson_id: str, status, children=None
    ) -> None:
        self.lesson_no = lesson_no
        self.lesson_name = lesson_name
        self.lesson_id = lesson_id
        self.children = children
        self.status = status

    def __json__(self):
        return {
            "lesson_no": self.lesson_no,
            "lesson_name": self.lesson_name,
            "lesson_id": self.lesson_id,
            "status": self.status,
            "children": self.children,
        }


@register_schema_to_swagger
class AICourseDTO:
    course_id: str
    course_name: str
    lessons: list[AILessonAttendDTO]

    def __init__(
        self,
        course_id: str,
        course_name: str,
        teach_avator: str,
        lessons: List[AILessonAttendDTO],
    ) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.teach_avator = teach_avator
        self.lessons = lessons

    def __json__(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "teach_avator": self.teach_avator,
            "lessons": self.lessons,
        }


@register_schema_to_swagger
class StudyRecordItemDTO:
    script_index: int
    script_role: str
    script_type: int
    script_content: str
    lesson_id: str
    id: str

    def __init__(
        self, script_index, script_role, script_type, script_content, lesson_id, id
    ):
        self.script_index = script_index
        self.script_role = script_role
        self.script_type = script_type
        self.script_content = script_content
        self.lesson_id = lesson_id
        self.id = id

    def __json__(self):
        return {
            "script_index": self.script_index,
            "script_role": self.script_role,
            "script_type": self.script_type,
            "script_content": self.script_content,
            "lesson_id": self.lesson_id,
            "id": self.id,
        }


@register_schema_to_swagger
class StudyUIDTO:
    type: str
    content: object
    lesson_id: str

    def __init__(self, type, content, lesson_id):
        self.type = type
        self.content = content
        self.lesson_id = lesson_id

    def __json__(self):
        return {"type": self.type, "content": self.content, "lesson_id": self.lesson_id}


@register_schema_to_swagger
class StudyRecordDTO:
    records: List[StudyRecordItemDTO]
    ui: StudyUIDTO
    ask_mode: bool
    teach_avator: str

    def __init__(self, records, ui=None, ask_mode=True, teach_avator=None):
        self.records = records
        self.ui = ui
        self.ask_mode = ask_mode
        self.teach_avator = teach_avator

    def __json__(self):
        return {
            "records": self.records,
            "ui": self.ui,
            "ask_mode": self.ask_mode,
            "teach_avator": self.teach_avator,
        }


@register_schema_to_swagger
class StudyRecordProgressDTO:
    lesson_id: str
    lesson_name: str
    lesson_no: str
    status: str
    script_index: int
    script_name: str
    is_branch: bool

    def __init__(
        self,
        lesson_id,
        lesson_name,
        lesson_no,
        status,
        script_index,
        script_name,
        is_branch,
    ):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
        self.lesson_no = lesson_no
        self.status = status
        self.script_index = script_index
        self.script_name = script_name
        self.is_branch = is_branch

    def __json__(self):
        return {
            "lesson_id": self.lesson_id,
            "lesson_name": self.lesson_name,
            "lesson_no": self.lesson_no,
            "status": self.status,
            "script_index": self.script_index,
            "script_name": self.script_name,
            "is_branch": self.is_branch,
        }


@register_schema_to_swagger
class ScriptInfoDTO:
    script_index: int
    script_name: str
    is_trial_lesson: bool

    def __init__(self, script_index, script_name, is_trial_lesson):
        self.script_index = script_index
        self.script_name = script_name
        self.is_trial_lesson = is_trial_lesson

    def __json__(self):
        return {
            "script_index": self.script_index,
            "script_name": self.script_name,
            "is_trial_lesson": self.is_trial_lesson,
        }
