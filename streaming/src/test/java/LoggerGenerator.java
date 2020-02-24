import org.apache.log4j.Logger;

public class LoggerGenerator {

    private final static Logger log = Logger.getLogger(LoggerGenerator.class);

    public static void main(String[] args) {
        int index = 0;
        while(true) {
            log.info("current value is " + index++);
        }
    }
}
