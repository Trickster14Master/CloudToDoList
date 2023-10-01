package ru.example.cloudtodolistandroid.data.models.note

data class NoteResult(
    val id: Int=0,
    val NameNote : String="",
    val DescriptionNote  : String="",
    val UserToken   : String="",
)

data class NotePost(
    val NameNote : String="",
    val DescriptionNote  : String="",
    val UserToken   : String="",
)
