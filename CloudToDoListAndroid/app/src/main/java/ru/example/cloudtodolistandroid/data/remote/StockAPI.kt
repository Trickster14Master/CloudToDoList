package ru.example.cloudtodolistandroid.data.remote

import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Query
import ru.example.cloudtodolistandroid.data.models.fail.FileResult
import ru.example.cloudtodolistandroid.data.models.grouptask.GroupTaskPost
import ru.example.cloudtodolistandroid.data.models.grouptask.GroupTaskResult
import ru.example.cloudtodolistandroid.data.models.note.NotePost
import ru.example.cloudtodolistandroid.data.models.note.NoteResult
import ru.example.cloudtodolistandroid.data.models.task.TaskResult
import ru.example.cloudtodolistandroid.data.models.taskforgroup.TaskForGroupPost
import ru.example.cloudtodolistandroid.data.models.taskforgroup.TaskForGroupResult
import ru.example.cloudtodolistandroid.data.models.user.AuthUser
import ru.example.cloudtodolistandroid.data.models.user.RegistrationUser
import ru.example.cloudtodolistandroid.data.models.user.UserToken

interface StockAPI {
    //GET

    @GET("NoteAPI/NoteAPI/")
    suspend fun getNote(@Query("search") userToken: String):Result<List<NoteResult>>

    @GET("FileAPI/FileAPI/")
    suspend fun getFile(@Query("search") userToken: String):Result<List<FileResult>>

    @GET("TaskAPI/TaskAPI/")
    suspend fun getTask(@Query("search") userToken: String):Result<List<TaskResult>>

    @GET("GroupTaskAPI/GroupTaskAPI/")
    suspend fun getGroupTask(@Query("search") userToken: String):Result<List<GroupTaskResult>>

    @GET("TaskForGroupAPI/TaskForGroupAPI/")
    suspend fun getTaskForGroup(@Query("search") userToken: String):Result<List<TaskForGroupResult>>

    //POST

    @POST("NoteAPI/NoteAPI/")
    suspend fun postNote(@Body notePost: NotePost):Result<NotePost>

    @POST("TaskForGroupAPI/TaskForGroupAPI/")
    suspend fun postTaskForGroup(@Body taskForGroupPost: TaskForGroupPost):Result<TaskForGroupPost>

    @POST("GroupTaskAPI/GroupTaskAPI/")
    suspend fun postGroupTask(@Body groupTaskPost: GroupTaskPost):Result<GroupTaskPost>

    @POST("ToDo/auth/user/")
    suspend fun registrationUser(@Body registrationUser: RegistrationUser):Result<RegistrationUser>

    @POST("auth/token/login/")
    suspend fun authUser(@Body authUser: AuthUser):Result<UserToken>
}