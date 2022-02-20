// 获取时间 格式：20201208200419
def getTime() {
    return new Date().format('yyyy-MM-dd HH:mm:ss')
}

def getJenkinsHome(){
	return "${JENKINS_HOME}";
}
def String getJobPath(){
	String jobName = "${JOB_NAME}";
	String[] temps = jobName.split("/");	
	jobName = temps[temps.length-1];	
	return getLocalJobPathByUrl("${JOB_URL}", jobName);    
}
def String getBuildPath(){
    return getJobPath() + "/builds/${BUILD_NUMBER}"
}

def getLocalJobPathByUrl(jobUrl, jobName){
	//println "getLocalJobPathByUrl:${jobUrl}";
	String[] urlSplits = jobUrl.split("/");  // http://xx.xx.xx.xx:8080/job/OAM_V20/job/mml_build_on_v20/149/	
	def jobPath = getJenkinsHome();
	int jobNum = 0;
	//for(subDir in urlSplits){
	for(int i=0;i<urlSplits.size();i++){
	    def subDir = urlSplits[i];
		//println subDir;
		if(subDir == "job"){
			subDir = "jobs"; 
			jobNum++;
			//if(jobNum>1)
			//   continue;
		}
		if(jobNum > 0){
			jobPath += "/${subDir}";
			if(subDir == jobName)
			break;
		}
	}
	//System.out.println(jobPath);	
	return jobPath;    	  
}

def saveEnvToXml() {
	def jobVariables = currentBuild.getBuildVariables();
	println "jobVariables:${jobVariables}"; 
	println "ROBOT_FAILEDCASES: ${ROBOT_FAILEDCASES}";  
	println "ROBOT_PASSRATIO: ${ROBOT_PASSRATIO}";  
	println "ROBOT_PASSED: ${ROBOT_PASSED}";  
	println "ROBOT_FAILED: ${ROBOT_FAILED}";  
	println "ROBOT_TOTAL: ${ROBOT_TOTAL}";  
	println "ROBOT_PASSPERCENTAGE: ${ROBOT_PASSPERCENTAGE}";               
	println "ROBOT_REPORTLINK: ${ROBOT_REPORTLINK}";  
}



