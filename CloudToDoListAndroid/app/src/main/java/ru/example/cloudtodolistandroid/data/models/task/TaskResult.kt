package ru.example.cloudtodolistandroid.data.models.task

data class TaskResult(
    val id:Int,
    val UserToken:String,
    val NameTask:String,
    val DescriptionTask:String,
    val DataTask:String,
    val StatusTask:Boolean,
    val FileForTask:String
)