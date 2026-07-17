%global debug_package %{nil}

%global __provides_exclude_from ^/opt/postman/.*$
%global __requires_exclude_from ^/opt/postman/.*$

Name:           postman
Version:        12.19.5
Release:        %autorelease
Summary:        Postman API Platform

License:        LicenseRef-postman-eula
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

%description
Build, test, and document your APIs faster.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/postman
cp -r * %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -s /opt/postman/Postman %{buildroot}%{_bindir}/postman

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/postman.desktop

install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
ln -s /opt/postman/app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%check

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog