package seminars.lesson_2.factorymethod;

import seminars.lesson_2.templatemethod.LogEntry;
import seminars.lesson_2.templatemethod.LogReader;

public class TextFileReader extends LogReader {
    @Override
    public Object getDataSource() {
        return null;
    }

    @Override
    public void setDataSource(Object data) {

    }

    @Override
    protected Iterable<String> readEntries(int position) {
        return null;
    }

    @Override
    protected LogEntry parseLogEntry(String stringEntry) {
        return null;
    }
}
