%global debug_package %{nil}

Name:           catppuccin-cursors
Version:        2.0.0
Release:        1%{?dist}
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch
BuildRequires:  unzip

Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%global release_url https://github.com/catppuccin/cursors/releases/download/v2.0.0

Source0:  %{release_url}/catppuccin-frappe-blue-cursors.zip
Source1:  %{release_url}/catppuccin-frappe-dark-cursors.zip
Source2:  %{release_url}/catppuccin-frappe-flamingo-cursors.zip
Source3:  %{release_url}/catppuccin-frappe-green-cursors.zip
Source4:  %{release_url}/catppuccin-frappe-lavender-cursors.zip
Source5:  %{release_url}/catppuccin-frappe-light-cursors.zip
Source6:  %{release_url}/catppuccin-frappe-maroon-cursors.zip
Source7:  %{release_url}/catppuccin-frappe-mauve-cursors.zip
Source8:  %{release_url}/catppuccin-frappe-peach-cursors.zip
Source9:  %{release_url}/catppuccin-frappe-pink-cursors.zip
Source10: %{release_url}/catppuccin-frappe-red-cursors.zip
Source11: %{release_url}/catppuccin-frappe-rosewater-cursors.zip
Source12: %{release_url}/catppuccin-frappe-sapphire-cursors.zip
Source13: %{release_url}/catppuccin-frappe-sky-cursors.zip
Source14: %{release_url}/catppuccin-frappe-teal-cursors.zip
Source15: %{release_url}/catppuccin-frappe-yellow-cursors.zip

Source16: %{release_url}/catppuccin-latte-blue-cursors.zip
Source17: %{release_url}/catppuccin-latte-dark-cursors.zip
Source18: %{release_url}/catppuccin-latte-flamingo-cursors.zip
Source19: %{release_url}/catppuccin-latte-green-cursors.zip
Source20: %{release_url}/catppuccin-latte-lavender-cursors.zip
Source21: %{release_url}/catppuccin-latte-light-cursors.zip
Source22: %{release_url}/catppuccin-latte-maroon-cursors.zip
Source23: %{release_url}/catppuccin-latte-mauve-cursors.zip
Source24: %{release_url}/catppuccin-latte-peach-cursors.zip
Source25: %{release_url}/catppuccin-latte-pink-cursors.zip
Source26: %{release_url}/catppuccin-latte-red-cursors.zip
Source27: %{release_url}/catppuccin-latte-rosewater-cursors.zip
Source28: %{release_url}/catppuccin-latte-sapphire-cursors.zip
Source29: %{release_url}/catppuccin-latte-sky-cursors.zip
Source30: %{release_url}/catppuccin-latte-teal-cursors.zip
Source31: %{release_url}/catppuccin-latte-yellow-cursors.zip

Source32: %{release_url}/catppuccin-macchiato-blue-cursors.zip
Source33: %{release_url}/catppuccin-macchiato-dark-cursors.zip
Source34: %{release_url}/catppuccin-macchiato-flamingo-cursors.zip
Source35: %{release_url}/catppuccin-macchiato-green-cursors.zip
Source36: %{release_url}/catppuccin-macchiato-lavender-cursors.zip
Source37: %{release_url}/catppuccin-macchiato-light-cursors.zip
Source38: %{release_url}/catppuccin-macchiato-maroon-cursors.zip
Source39: %{release_url}/catppuccin-macchiato-mauve-cursors.zip
Source40: %{release_url}/catppuccin-macchiato-peach-cursors.zip
Source41: %{release_url}/catppuccin-macchiato-pink-cursors.zip
Source42: %{release_url}/catppuccin-macchiato-red-cursors.zip
Source43: %{release_url}/catppuccin-macchiato-rosewater-cursors.zip
Source44: %{release_url}/catppuccin-macchiato-sapphire-cursors.zip
Source45: %{release_url}/catppuccin-macchiato-sky-cursors.zip
Source46: %{release_url}/catppuccin-macchiato-teal-cursors.zip
Source47: %{release_url}/catppuccin-macchiato-yellow-cursors.zip

Source48: %{release_url}/catppuccin-mocha-blue-cursors.zip
Source49: %{release_url}/catppuccin-mocha-dark-cursors.zip
Source50: %{release_url}/catppuccin-mocha-flamingo-cursors.zip
Source51: %{release_url}/catppuccin-mocha-green-cursors.zip
Source52: %{release_url}/catppuccin-mocha-lavender-cursors.zip
Source53: %{release_url}/catppuccin-mocha-light-cursors.zip
Source54: %{release_url}/catppuccin-mocha-maroon-cursors.zip
Source55: %{release_url}/catppuccin-mocha-mauve-cursors.zip
Source56: %{release_url}/catppuccin-mocha-peach-cursors.zip
Source57: %{release_url}/catppuccin-mocha-pink-cursors.zip
Source58: %{release_url}/catppuccin-mocha-red-cursors.zip
Source59: %{release_url}/catppuccin-mocha-rosewater-cursors.zip
Source60: %{release_url}/catppuccin-mocha-sapphire-cursors.zip
Source61: %{release_url}/catppuccin-mocha-sky-cursors.zip
Source62: %{release_url}/catppuccin-mocha-teal-cursors.zip
Source63: %{release_url}/catppuccin-mocha-yellow-cursors.zip

%description
Meta package for all Catppuccin cursor themes.

%package frappe
Summary:        Catppuccin Frappé cursor themes
%description frappe
Catppuccin Frappé cursor themes in all accent colors.
%files frappe
%license */catppuccin-frappe-*-cursors/LICENSE
%doc */catppuccin-frappe-*-cursors/AUTHORS
%{_datadir}/icons/catppuccin-frappe-*-cursors/

%package latte
Summary:        Catppuccin Latte cursor themes
%description latte
Catppuccin Latte cursor themes in all accent colors.
%files latte
%license */catppuccin-latte-*-cursors/LICENSE
%doc */catppuccin-latte-*-cursors/AUTHORS
%{_datadir}/icons/catppuccin-latte-*-cursors/

%package macchiato
Summary:        Catppuccin Macchiato cursor themes
%description macchiato
Catppuccin Macchiato cursor themes in all accent colors.
%files macchiato
%license */catppuccin-macchiato-*-cursors/LICENSE
%doc */catppuccin-macchiato-*-cursors/AUTHORS
%{_datadir}/icons/catppuccin-macchiato-*-cursors/

%package mocha
Summary:        Catppuccin Mocha cursor themes
%description mocha
Catppuccin Mocha cursor themes in all accent colors.
%files mocha
%license */catppuccin-mocha-*-cursors/LICENSE
%doc */catppuccin-mocha-*-cursors/AUTHORS
%{_datadir}/icons/catppuccin-mocha-*-cursors/

%prep
%setup -c -T

unzip -q %{SOURCE0} -d catppuccin-frappe-blue-cursors
unzip -q %{SOURCE1} -d catppuccin-frappe-dark-cursors
unzip -q %{SOURCE2} -d catppuccin-frappe-flamingo-cursors
unzip -q %{SOURCE3} -d catppuccin-frappe-green-cursors
unzip -q %{SOURCE4} -d catppuccin-frappe-lavender-cursors
unzip -q %{SOURCE5} -d catppuccin-frappe-light-cursors
unzip -q %{SOURCE6} -d catppuccin-frappe-maroon-cursors
unzip -q %{SOURCE7} -d catppuccin-frappe-mauve-cursors
unzip -q %{SOURCE8} -d catppuccin-frappe-peach-cursors
unzip -q %{SOURCE9} -d catppuccin-frappe-pink-cursors
unzip -q %{SOURCE10} -d catppuccin-frappe-red-cursors
unzip -q %{SOURCE11} -d catppuccin-frappe-rosewater-cursors
unzip -q %{SOURCE12} -d catppuccin-frappe-sapphire-cursors
unzip -q %{SOURCE13} -d catppuccin-frappe-sky-cursors
unzip -q %{SOURCE14} -d catppuccin-frappe-teal-cursors
unzip -q %{SOURCE15} -d catppuccin-frappe-yellow-cursors

unzip -q %{SOURCE16} -d catppuccin-latte-blue-cursors
unzip -q %{SOURCE17} -d catppuccin-latte-dark-cursors
unzip -q %{SOURCE18} -d catppuccin-latte-flamingo-cursors
unzip -q %{SOURCE19} -d catppuccin-latte-green-cursors
unzip -q %{SOURCE20} -d catppuccin-latte-lavender-cursors
unzip -q %{SOURCE21} -d catppuccin-latte-light-cursors
unzip -q %{SOURCE22} -d catppuccin-latte-maroon-cursors
unzip -q %{SOURCE23} -d catppuccin-latte-mauve-cursors
unzip -q %{SOURCE24} -d catppuccin-latte-peach-cursors
unzip -q %{SOURCE25} -d catppuccin-latte-pink-cursors
unzip -q %{SOURCE26} -d catppuccin-latte-red-cursors
unzip -q %{SOURCE27} -d catppuccin-latte-rosewater-cursors
unzip -q %{SOURCE28} -d catppuccin-latte-sapphire-cursors
unzip -q %{SOURCE29} -d catppuccin-latte-sky-cursors
unzip -q %{SOURCE30} -d catppuccin-latte-teal-cursors
unzip -q %{SOURCE31} -d catppuccin-latte-yellow-cursors

unzip -q %{SOURCE32} -d catppuccin-macchiato-blue-cursors
unzip -q %{SOURCE33} -d catppuccin-macchiato-dark-cursors
unzip -q %{SOURCE34} -d catppuccin-macchiato-flamingo-cursors
unzip -q %{SOURCE35} -d catppuccin-macchiato-green-cursors
unzip -q %{SOURCE36} -d catppuccin-macchiato-lavender-cursors
unzip -q %{SOURCE37} -d catppuccin-macchiato-light-cursors
unzip -q %{SOURCE38} -d catppuccin-macchiato-maroon-cursors
unzip -q %{SOURCE39} -d catppuccin-macchiato-mauve-cursors
unzip -q %{SOURCE40} -d catppuccin-macchiato-peach-cursors
unzip -q %{SOURCE41} -d catppuccin-macchiato-pink-cursors
unzip -q %{SOURCE42} -d catppuccin-macchiato-red-cursors
unzip -q %{SOURCE43} -d catppuccin-macchiato-rosewater-cursors
unzip -q %{SOURCE44} -d catppuccin-macchiato-sapphire-cursors
unzip -q %{SOURCE45} -d catppuccin-macchiato-sky-cursors
unzip -q %{SOURCE46} -d catppuccin-macchiato-teal-cursors
unzip -q %{SOURCE47} -d catppuccin-macchiato-yellow-cursors

unzip -q %{SOURCE48} -d catppuccin-mocha-blue-cursors
unzip -q %{SOURCE49} -d catppuccin-mocha-dark-cursors
unzip -q %{SOURCE50} -d catppuccin-mocha-flamingo-cursors
unzip -q %{SOURCE51} -d catppuccin-mocha-green-cursors
unzip -q %{SOURCE52} -d catppuccin-mocha-lavender-cursors
unzip -q %{SOURCE53} -d catppuccin-mocha-light-cursors
unzip -q %{SOURCE54} -d catppuccin-mocha-maroon-cursors
unzip -q %{SOURCE55} -d catppuccin-mocha-mauve-cursors
unzip -q %{SOURCE56} -d catppuccin-mocha-peach-cursors
unzip -q %{SOURCE57} -d catppuccin-mocha-pink-cursors
unzip -q %{SOURCE58} -d catppuccin-mocha-red-cursors
unzip -q %{SOURCE59} -d catppuccin-mocha-rosewater-cursors
unzip -q %{SOURCE60} -d catppuccin-mocha-sapphire-cursors
unzip -q %{SOURCE61} -d catppuccin-mocha-sky-cursors
unzip -q %{SOURCE62} -d catppuccin-mocha-teal-cursors
unzip -q %{SOURCE63} -d catppuccin-mocha-yellow-cursors

mkdir -p doc_meta
cp -a catppuccin-*_cursors/LICENSE doc_meta/ || :
cp -a catppuccin-*_cursors/AUTHORS doc_meta/ || :

%build

%install
install -dm755 %{buildroot}%{_datadir}/icons

define install_cursor() \
install -dm755 %{buildroot}%{_datadir}/icons/%{1} \
cp -a %{1}/* %{buildroot}%{_datadir}/icons/%{1}/ \
rm -f %{buildroot}%{_datadir}/icons/%{1}/LICENSE \
rm -f %{buildroot}%{_datadir}/icons/%{1}/AUTHORS \
%{nil}

%install_cursor catppuccin-frappe-blue-cursors
%install_cursor catppuccin-frappe-dark-cursors
%install_cursor catppuccin-frappe-flamingo-cursors
%install_cursor catppuccin-frappe-green-cursors
%install_cursor catppuccin-frappe-lavender-cursors
%install_cursor catppuccin-frappe-light-cursors
%install_cursor catppuccin-frappe-maroon-cursors
%install_cursor catppuccin-frappe-mauve-cursors
%install_cursor catppuccin-frappe-peach-cursors
%install_cursor catppuccin-frappe-pink-cursors
%install_cursor catppuccin-frappe-red-cursors
%install_cursor catppuccin-frappe-rosewater-cursors
%install_cursor catppuccin-frappe-sapphire-cursors
%install_cursor catppuccin-frappe-sky-cursors
%install_cursor catppuccin-frappe-teal-cursors
%install_cursor catppuccin-frappe-yellow-cursors

%install_cursor catppuccin-latte-blue-cursors
%install_cursor catppuccin-latte-dark-cursors
%install_cursor catppuccin-latte-flamingo-cursors
%install_cursor catppuccin-latte-green-cursors
%install_cursor catppuccin-latte-lavender-cursors
%install_cursor catppuccin-latte-light-cursors
%install_cursor catppuccin-latte-maroon-cursors
%install_cursor catppuccin-latte-mauve-cursors
%install_cursor catppuccin-latte-peach-cursors
%install_cursor catppuccin-latte-pink-cursors
%install_cursor catppuccin-latte-red-cursors
%install_cursor catppuccin-latte-rosewater-cursors
%install_cursor catppuccin-latte-sapphire-cursors
%install_cursor catppuccin-latte-sky-cursors
%install_cursor catppuccin-latte-teal-cursors
%install_cursor catppuccin-latte-yellow-cursors

%install_cursor catppuccin-macchiato-blue-cursors
%install_cursor catppuccin-macchiato-dark-cursors
%install_cursor catppuccin-macchiato-flamingo-cursors
%install_cursor catppuccin-macchiato-green-cursors
%install_cursor catppuccin-macchiato-lavender-cursors
%install_cursor catppuccin-macchiato-light-cursors
%install_cursor catppuccin-macchiato-maroon-cursors
%install_cursor catppuccin-macchiato-mauve-cursors
%install_cursor catppuccin-macchiato-peach-cursors
%install_cursor catppuccin-macchiato-pink-cursors
%install_cursor catppuccin-macchiato-red-cursors
%install_cursor catppuccin-macchiato-rosewater-cursors
%install_cursor catppuccin-macchiato-sapphire-cursors
%install_cursor catppuccin-macchiato-sky-cursors
%install_cursor catppuccin-macchiato-teal-cursors
%install_cursor catppuccin-macchiato-yellow-cursors

%install_cursor catppuccin-mocha-blue-cursors
%install_cursor catppuccin-mocha-dark-cursors
%install_cursor catppuccin-mocha-flamingo-cursors
%install_cursor catppuccin-mocha-green-cursors
%install_cursor catppuccin-mocha-lavender-cursors
%install_cursor catppuccin-mocha-light-cursors
%install_cursor catppuccin-mocha-maroon-cursors
%install_cursor catppuccin-mocha-mauve-cursors
%install_cursor catppuccin-mocha-peach-cursors
%install_cursor catppuccin-mocha-pink-cursors
%install_cursor catppuccin-mocha-red-cursors
%install_cursor catppuccin-mocha-rosewater-cursors
%install_cursor catppuccin-mocha-sapphire-cursors
%install_cursor catppuccin-mocha-sky-cursors
%install_cursor catppuccin-mocha-teal-cursors
%install_cursor catppuccin-mocha-yellow-cursors

%files

%changelog
%autochangelog
