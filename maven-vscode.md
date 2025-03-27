# -> No need to install maven externally already installed by the java package installer in vs code.

# -> If the old cache of maven directory remains <ins>file</ins> to <ins>preferneces</ins> to <ins>settings</ins> to <ins> search maven in search bar</ins> to change executables,path, prefer maven wrapper to reset to default mode.

# -> Install apache maven and place the unzipped in c/programfiles location(same as apache tomcat server).Then copy the bin path and add to the edit envirment variable as MVN_HOME(same as JAVA_HOME JDK more than 11 versions). Then mvn command and mvn clean works.

# -> `mvn clean package` command in the project directory location creates the target file.

# -> https://code.visualstudio.com/docs/java/java-tomcat-jetty

# -> Working with Application Servers in VS Code 

# -> use server actions(open in browser first link) then add deployment then server then server actions(open in browser second link) then publish server(full)

# -> don't use the relocated from versions of dependancies , use only relocated to versions of dependancy .Else you will get lot of errors in packaging.

# -> some dependancies already included in other dependancies.No need to import those dependancies.Ex jakarta persistance included in org.hibernate.orm.

# -> never comment code in jsp files as it reads comments also and take the comments also into conideration.It will not run and give lot of errors.
