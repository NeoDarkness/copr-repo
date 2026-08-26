%global forgeurl https://github.com/ryanoasis/nerd-fonts

Version:        3.5.1

%forgemeta

Name:           nerd-fonts
Release:        %autorelease
Summary:        Iconic font aggregator, collection, and patcher

License:        MIT AND OFL-1.1
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
Nerd Fonts is a collection of developer-targeted fonts patched with
additional glyphs and icons.

%package firamono
Summary:        Fira Mono Nerd Font
License:        OFL-1.1

Requires:       fontpackages-filesystem

%description firamono
Fira Mono patched with Nerd Fonts glyphs.

%package firacode
Summary:        Fira Code Nerd Font
License:        OFL-1.1
	
Requires:       fontpackages-filesystem

%description firacode
Fira Code patched with Nerd Fonts glyphs.

%prep
%forgeautosetup -p1

%build

%install
install -d %{buildroot}%{_fontdir}
install -m 0644 patched-fonts/FiraMono/*.ttf %{buildroot}%{_fontdir}
install -m 0644 patched-fonts/FiraCode/*.ttf %{buildroot}%{_fontdir}

%check

%files
%license LICENSE
%doc README.md

%files firamono
%license patched-fonts/FiraMono/LICENSE
%doc patched-fonts/FiraMono/README.md
%_font_pkg FiraMonoNerdFont*.ttf

%files firacode
%license patched-fonts/FiraCode/LICENSE
%doc patched-fonts/FiraCode/README.md
%_font_pkg FiraCodeNerdFont*.ttf

%changelog
%autochangelog