import { HEADER_NAV } from "../../utils/constants";
import type { ViewId } from "../../types";

interface HeaderProps {
  activeView: ViewId;
  showView: (view: ViewId) => void;
  handleAction: (event: React.MouseEvent<HTMLElement>, action: string) => void;
}

export default function Header({ activeView, showView, handleAction }: HeaderProps) {
  return (
    <header className="w-full h-20 sticky top-0 bg-transparent flex items-center justify-between px-12 z-50 shadow-none focus-transition">
      <div className="flex items-center gap-8 flex-1 justify-end">
        <nav className="hidden md:flex gap-2 font-['Manrope'] font-bold tracking-tight text-sm">
          {HEADER_NAV.map((item) => (
            <button
              key={item.id}
              type="button"
              onClick={() => showView(item.id)}
              className={[
                "px-4 py-2 rounded-xl transition-all duration-200",
                activeView === item.id ? "text-white bg-white/10" : "text-white/60 hover:text-white hover:bg-white/5"
              ].join(" ")}
            >
              {item.label}
            </button>
          ))}
        </nav>
        <div className="flex items-center gap-6 ml-4">
          <button
            type="button"
            onClick={(event) => handleAction(event, "Login")}
            className="text-white hover:text-white/80 transition-colors font-bold text-sm"
          >
            Log In
          </button>
          <button
            type="button"
            onClick={(event) => handleAction(event, "Registration")}
            className="px-6 py-2 bg-black text-white font-headline font-bold rounded-full text-sm shadow-[0_0_15px_rgba(176,127,241,0.5)] btn-interact"
          >
            Join Now
          </button>
        </div>
      </div>
    </header>
  );
}
