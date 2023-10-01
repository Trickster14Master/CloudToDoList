package ru.example.cloudtodolistandroid.data.remote

import retrofit2.http.Body
import ru.example.cloudtodolistandroid.data.models.grouptask.GroupTaskPost
import ru.example.cloudtodolistandroid.data.models.note.NotePost
import ru.example.cloudtodolistandroid.data.models.taskforgroup.TaskForGroupPost
import ru.example.cloudtodolistandroid.data.models.user.AuthUser
import ru.example.cloudtodolistandroid.data.models.user.RegistrationUser
import ru.example.cloudtodolistandroid.data.models.user.UserToken
import javax.inject.Inject

class RemoteDataSourceNote @Inject constructor(private val baseService:StockAPI){
    suspend fun getNote(userToken: String) = baseService.getNote(userToken=userToken)
    suspend fun postNote(body: NotePost) = baseService.postNote(body)

}

class RemoteDataSourceFile @Inject constructor(private val baseService:StockAPI){
    suspend fun getFile(userToken: String) = baseService.getFile(userToken=userToken)

}

class RemoteDataSourceTask @Inject constructor(private val baseService:StockAPI){
    suspend fun getTask(userToken: String) = baseService.getTask(userToken=userToken)

}

class RemoteDataSourceGroupTask @Inject constructor(private val baseService:StockAPI){
    suspend fun getGroupTask(userToken: String) = baseService.getGroupTask(userToken=userToken)
    suspend fun postGroupTask(body: GroupTaskPost) = baseService.postGroupTask(groupTaskPost=body)

}

class RemoteDataTaskForGroup @Inject constructor(private val baseService:StockAPI){
    suspend fun getTaskForGroup(userToken: String) = baseService.getTaskForGroup(userToken=userToken)
    suspend fun postTaskForGroup(taskForGroupPost: TaskForGroupPost) = baseService.postTaskForGroup(taskForGroupPost = taskForGroupPost)
}

class RemoteDataUser @Inject constructor(private val baseService: StockAPI){
    suspend fun registrationUser(registrationUser:RegistrationUser) = baseService.registrationUser(registrationUser=registrationUser)
    suspend fun authUser(authUser: AuthUser) = baseService.authUser(authUser=authUser)
}

