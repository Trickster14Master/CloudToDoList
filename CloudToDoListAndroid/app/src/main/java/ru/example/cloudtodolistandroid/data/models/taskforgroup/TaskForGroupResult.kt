package ru.example.cloudtodolistandroid.data.models.taskforgroup

data class TaskForGroupResult(
    val id:Int,
    val UserToken:String,
    val NameTaskForGroup:String,
    val DescriptionTask:String,
    val StatusTaskForGroup:Boolean,
    val Group:Int,
)