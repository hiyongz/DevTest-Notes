//function: 将job的构建结果增加到流水线结果xml中，置流水线结果(使用job结果改变流水线的成功失败)
//@Library('lib@1.0') import com.*
//def cp1 = build job: 'oam_compile', propagate: false    
//setStageBuild('compile', cp1);

//enter:
def call(stageName, job, owner) {    
	
	//println "Set ${stageName}:${job.absoluteUrl}:${owner}";
	initXmlFile();
	
	if(job instanceof String) {
		saveToXml(stageName, job, owner);
		return;
	}    
    
    if (stageName=="autotest") {
        saveRFResultsToXml(stageName, job, owner)
    } else {
        //设置stage结果
        saveToXml(stageName, job.absoluteUrl, job.result, owner);
    }	
	
	//刷新流水线结果
	if(job.result!='ABORTED'){
	  currentBuild.result = job.result
	}
	
	//失败流水线退出
	if(job.result=='FAILURE'){	    
		error "${job.absoluteUrl} fail!"
	}
}

def getXmlFile() {
	def final XML_FILE="pipeline.xml";	
	return getBuildPath() + "/${XML_FILE}";	
}

def getJenkinsHome(){
	return "${JENKINS_HOME}";
}
def String getJobPath(){
	String jobName = "${JOB_NAME}";
	//println "getJobPath:${jobName}";
	String[] temps = jobName.split("/");	
	jobName = temps[temps.length-1];	
	//println "getJobPath->${jobName}";
	return getLocalJobPathByUrl("${JOB_URL}", jobName);    
}
def String getBuildPath(){
    return getJobPath() + "/builds/${BUILD_NUMBER}"
}

//@NonCPS
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

def getClassifyByUrl(jobUrl){	
	String[] urlSplits = jobUrl.split("/job/");  // http://xx.xx.xx.xx:8080/job/OAM_V20/job/mml_build_on_v20/149/
	
	if(urlSplits.length<3){
		return '';
	}
	
	return urlSplits[urlSplits.length-2]; //job上一级folder
}

def initXmlFile(){	
	def xmlFile = getXmlFile();
    if(new File(xmlFile).exists()){
		//println "${xmlFile} has exists!"
		return;
	}
	
	def root="""<?xml version="1.0" encoding="UTF-8"?>
<pipeline url="${BUILD_URL}">
</pipeline>"""
	
	def fileWriter = new FileWriter(xmlFile);	
	fileWriter.write(root);
	fileWriter.close();	
}

def saveToXml(stageName, jobResult, jobOwner){
  
  //if(!waitSignal())
  //	return false;
  
	def xmlFile = getXmlFile();
	def pipeline = new XmlParser().parse(xmlFile);
	def bAdded = false;
	for(stage in pipeline.stage){
		if(stage.attribute("name")==stageName){					
			def atts = stage.attributes();			
			//atts.put('jobnum', (atts.get('jobnum').toInteger()+1) as String);
			if(jobResult=='FAILURE' || jobResult=='UNSTABLE' && atts.get('result') != 'FAILURE' || atts.get('result') == '' || atts.get('result') == 'ABORTED'){
				atts.put('result', jobResult);  
				println "[${stageName}] set result: ${jobResult}";
			}
			bAdded = true;
			break;
		}
	}
	if(!bAdded){
		def stage = pipeline.appendNode("stage", ['name':(stageName), 'jobnum':'0', 'result':(jobResult)]);
        println "[${stageName}] set result: ${jobResult}";
	}
	def fileWriter = new FileWriter(xmlFile);	
	fileWriter.write(groovy.xml.XmlUtil.serialize(pipeline));
	fileWriter.close();	
	
	//releaseSignal();
	//return true;
}

def saveToXml(stageName, jobUrl, jobResult, jobOwner){

	//if(!waitSignal())
  //	return false;
  	
	def xmlFile = getXmlFile();  
    println "[${stageName}] xmlFile: ${xmlFile}";    
	def pipeline = new XmlParser().parse(xmlFile);
	def bAdded = false;
	for(stage in pipeline.stage){
        def aaa = stage.attribute("name");
		if(stage.attribute("name")==stageName){
            println "[33333333333333333: ${aaa}]"
			stage.appendNode("job", ['url':(jobUrl), 'result':(jobResult), 'classify':(getClassifyByUrl(jobUrl)), 'owner':(jobOwner)]);	
			def atts = stage.attributes();			
			atts.put('jobnum', (atts.get('jobnum').toInteger()+1) as String);
			if(jobResult=='FAILURE' || jobResult=='UNSTABLE' && atts.get('result') != 'FAILURE' || atts.get('result') == '' || atts.get('result') == 'ABORTED'){
				atts.put('result', jobResult); 
				println "[${stageName}] set result: ${jobResult}";
			}
			bAdded = true;
			break;
		}
	}
	if(!bAdded){
		def stage = pipeline.appendNode("stage", ['name':(stageName), 'jobnum':'1', 'result':(jobResult)]);
		stage.appendNode("job", ['url':(jobUrl), 'result':(jobResult), 'classify':(getClassifyByUrl(jobUrl)), 'owner':(jobOwner)]);		
        println "[${stageName}] set result: ${jobResult}";
	}
	def fileWriter = new FileWriter(xmlFile);	
	fileWriter.write(groovy.xml.XmlUtil.serialize(pipeline));
	fileWriter.close();	
	
	//releaseSignal();
	//return true;
}

def saveRFResultsToXml(stageName, job, owner){
    // curl读取测试结果
    def WORKFLOW_API_JSON = sh ( script: "API_JSON=\$(curl -k --silent -L --user zhanghaiyong:11910f7bc9174575a89aaaa9247b516d21 ${job.absoluteUrl}/api/xml | tr '<' '\n' | egrep '^totalCount>|^failCount>' | sed 's/>/:/g'  | sed -e '1s/\$/,/g' | tr -d '\n'); echo \${API_JSON}", returnStdout: true ).trim();
    
    rf_results = WORKFLOW_API_JSON.split(",");
    if (rf_results[0]) {
        for ( res in rf_results ) {
            if (res.contains("failCount")) {
                failCount = res.split("failCount:")[1];
            }
            if (res.contains("totalCount")) {
                totalCount = res.split("totalCount:")[1];
            }
        }
        passCount = totalCount.toInteger() - failCount.toInteger();
        passPercentage = passCount/totalCount.toInteger() * 100;
        passPercentage = Math.round(passPercentage * 100) / 100;
        passRatio = passCount + " / " + totalCount;
        
    } else {
        passPercentage = 'null'; 
        passRatio = 'null'; 
    }    
    
    def currentUrl = currentBuild.absoluteUrl;
    def currentResult = currentBuild.currentResult;
    def Causes = currentBuild.getBuildCauses().shortDescription[0];
    def duration = currentBuild.durationString;
    def startTimeInMillis = currentBuild.startTimeInMillis;
    def startTime = new Date( startTimeInMillis ).toString();
    def jobVariables = job.getBuildVariables();
    
	def xmlFile = getXmlFile();  
    println "[${stageName}] xmlFile: ${xmlFile}";  

	def pipeline = new XmlParser().parse(xmlFile);
	def bAdded = false;
	for(stage in pipeline.stage){
		if(stage.attribute("name")==stageName){
			stage.appendNode("job", ['url':(job.absoluteUrl), 'jobname':(jobVariables.JOB_BASE_NAME), 'joburl':(jobVariables.JOB_URL), 'result':(job.result), 'log':(jobVariables.LOG), 'classify':(getClassifyByUrl(job.absoluteUrl)), 'owner':(owner), "robot_passpercentage":passPercentage, "robot_passratio":passRatio, 'currenturl':(currentUrl), 'currentresult':(currentResult), 'causes':(Causes), 'duration':(duration), 'starttime':startTime]]);
			def atts = stage.attributes();			
			atts.put('jobnum', (atts.get('jobnum').toInteger()+1) as String);
			if(job.result=='FAILURE' || job.result=='UNSTABLE' && atts.get('result') != 'FAILURE' || atts.get('result') == '' || atts.get('result') == 'ABORTED'){
				atts.put('result', job.result);
				println "[${stageName}] set result: ${job.result}";
			}
			bAdded = true;
			break;
		}
	}
	if(!bAdded){
		def stage = pipeline.appendNode("stage", ['name':(stageName), 'jobnum':'1', 'result':(job.result)]);
        stage.appendNode("job", ['url':(job.absoluteUrl), 'jobname':(jobVariables.JOB_BASE_NAME), 'joburl':(jobVariables.JOB_URL), 'result':(job.result), 'log':(jobVariables.LOG), 'classify':(getClassifyByUrl(job.absoluteUrl)), 'owner':(owner), "robot_passpercentage":passPercentage, "robot_passratio":passRatio, 'currenturl':(currentUrl), 'currentresult':(currentResult), 'causes':(Causes), 'duration':(duration), 'starttime':startTime]);		
        println "[${stageName}] set result: ${job.result}";
	}
	def fileWriter = new FileWriter(xmlFile);	
	fileWriter.write(groovy.xml.XmlUtil.serialize(pipeline));
	fileWriter.close();
}


def getSignalFile() {
	def final SIGNAL_FILE="signal.001";	
	//return getBuildPath() + "/${SIGNAL_FILE}";	
	return SIGNAL_FILE;
}

def waitSignal(){	
	def t1 = System.currentTimeMillis();	
	while(System.currentTimeMillis()-t1<10000){
		if(!(new File(getSignalFile()).exists())){
			new File(getSignalFile()).write(String.valueOf(System.currentTimeMillis()));
			return true;
		}		
		Thread.sleep(500);			
	}		
	return false;		
}

def releaseSignal(){	
	if((new File(getSignalFile()).exists())){
		new File(getSignalFile()).delete();		
	}
}


//call("compile", "http://127.0.0.1:8080/job/oam_compile/9/")
//call("compile", "http://127.0.0.1:8080/job/oam_compile/10/")
//call("ut", "http://127.0.0.1:8080/job/oam_ut/9/")